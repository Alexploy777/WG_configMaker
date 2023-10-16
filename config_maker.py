import sys
from PyQt5.QtWidgets import *

from gui import Ui_MainWindow
from config_maker_class import ConfigMaker



class WgConfig(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WgConfig, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('Генератор конфигурации')
        self.configmaker = ConfigMaker(self)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        # [Interface]
        self.ConfigName: str = self.lineEdit_config_name.text()
        self.PrivateKey: str = self.lineEdit_PrivateKey.text()
        self.Address: str = self.lineEdit_Address_1.text() + ', ' + self.lineEdit_Address_2.text()
        self.DNS: str = self.lineEdit_DNS.text()
        # # [Peer]
        self.PublicKey: str = self.lineEdit_PublicKey.text()
        self.AllowedIPs: str = self.lineEdit_AllowedIPs.text()
        self.Endpoint: str = self.lineEdit_Endpoint.text()
        if self.ConfigName and self.PrivateKey and self.lineEdit_Address_1.text() and self.DNS and self.PublicKey and self.AllowedIPs and self.Endpoint :
            self.configmaker.config_maker()
        else:
            QMessageBox.critical(self, 'Ошибка', f'Заполните все поля!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WgConfig()
    w.show()
    sys.exit(app.exec_())