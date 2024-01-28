from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal
from pytube import YouTube, request
from PySide6.QtWidgets import (QMainWindow, QApplication, QMessageBox, QWidget)
from frmMain import Ui_MainWindow
from frmDownloadStatus import Ui_frmDownloadStatus
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btDownload.clicked.connect(self.WindowDownload)
        self.OtherWindowDownload = []
    
    def WindowDownload(self):
        url = self.txtLink.text()
        titulo = self.txtTitulo.text() 


        if url == "":
            MensagemCampoEmBranco('Link')
            return None         

        # Define resolução e extensão do arquivo           
        if self.rbMp4.isChecked():
            tipo = 'video'       
        elif self.rbMp3.isChecked():
            tipo = 'audio' 

        self.w = DownloadStatus(url, titulo, tipo)
        self.w.show()
        self.OtherWindowDownload.append(self.w)

def MensagemDownloadFinalizado():
    dlg = QMessageBox()
    dlg.setWindowTitle("Informação")
    dlg.setText("Download feito com sucesso!")
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.setIcon(QMessageBox.Icon.Information)
    dlg.exec() 

def MensagemCampoEmBranco(campo:str):
    dlg = QMessageBox()
    dlg.setWindowTitle("Erro")
    dlg.setText(f"Campo {campo} em branco.")
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.setIcon(QMessageBox.Icon.Critical)
    dlg.exec()     

class DownloadStatus(QWidget, Ui_frmDownloadStatus):
    def __init__(self, url, titulo, tipo, parent=None):
        super().__init__(parent)
        self.setupUi(self)      
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)   
        self.url = url
        self.titulo = titulo              
        self.tipo = tipo
        self.progressBar.setValue(0)
        self.setWindowTitle('Downloading ' + self.titulo)
        self.btCancelar.clicked.connect(self.on_cancelButton_clicked)
        self.btPausar.clicked.connect(self.on_pauseButton_clicked)

        #### Create a download thread  
        self.downloadThread = downloadThread(self.url, self.titulo, self.tipo)
        self.downloadThread.download_process_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()     

    # Setting progress bar
    def set_progressbar_value(self, value):
        self.progressBar.setValue(value)
        if value == 100 and self.downloadThread.isFinished:
            MensagemDownloadFinalizado()  
            self.downloadThread.terminate()
            self.close()
 
    def on_cancelButton_clicked(self):
        self.downloadThread.is_cancelled = True
        self.downloadThread.terminate()
        # Fecha a janela de status de download
        self.close()     

    def on_pauseButton_clicked(self):
        if not self.downloadThread.is_paused:
            self.btPausar.setText('Continuar')
            self.downloadThread.is_paused = True  
        else:       
            self.btPausar.setText('Pausar')
            self.downloadThread.is_paused = False  

class downloadThread(QThread):
    download_process_signal = Signal(int)                        #Create signal
 
    def __init__(self, url:str, titulo:str, tipo:str):
        super(downloadThread, self).__init__()
        self.url = url
        self.titulo = titulo
        self.tipo = tipo  
        self.is_cancelled = False      
        self.is_paused = False      
 
    def run(self):
        try:
            yt = YouTube(self.url)
            if self.tipo =='video':
                self._arquivo = yt.streams.get_highest_resolution()
                filesize = self._arquivo.filesize  # get the video size
                if self.titulo != '':
                    filename = self.titulo + '.mp4'                
                else:
                    filename = AcceptableFileName(self._arquivo.title) + '.mp4'
            else:
                self._arquivo = yt.streams.filter(only_audio=True).first()
                filesize = self._arquivo.filesize  # get the video size
                if self.titulo != '':
                    filename = self.titulo + '.mp3'                
                else:
                    filename = AcceptableFileName(self._arquivo.title) + '.mp3'

            with open(filename, 'wb') as f:
                self._arquivo = request.stream(self._arquivo.url) # get an iterable stream
                downloaded = 0
                while True:
                    if self.is_cancelled:
                        break
                    if self.is_paused:
                        continue
                    chunk = next(self._arquivo, None) # get next chunk of video
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        process = downloaded / filesize * 100          
                        self.download_process_signal.emit(int(process))                             
            
            f.close()
            self.exit(0)  #Close thread
            
 
        except Exception as e:
            print(e)

def AcceptableFileName(filename): 
    filename = filename.replace('?', '').replace('>', '-').replace('<', '-')                 
    filename = filename.replace(':', ' ').replace('"', '').replace('/', '-')                 
    filename = filename.replace('\\', ' ').replace('|', ' ').replace('*', '')
    filename = filename.replace('`', '')  
    return filename 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.setWindowTitle("Download mp3/mp4 Youtube")
    mainwindow.show()
    app.exec()