import re
import sys

from PyQt5.QtWidgets import *

from config_maker_class import ConfigMaker
from gui import Ui_MainWindow


class WgConfig(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WgConfig, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('Генератор конфигурации')
        self.configmaker = ConfigMaker(self)
        self.pushButton_safe.clicked.connect(self.start)
        self.pushButton_open.clicked.connect(self.configmaker.config_reader)

    def start(self):
        name_list_required = ['PrivateKey', 'Address', 'DNS', 'PublicKey', 'AllowedIPs', 'Endpoint']
        flag_good = True
        name_list_dict = {}
        name_list_full = self.__dict__.keys()
        pattern = r'(^lineEdit)_(\w+)'
        for item in name_list_full:
            item_chose = re.match(pattern, item)
            if item_chose:
                name_list_dict[item_chose.group(2)] = getattr(self, item_chose.group(0)).text()

        for name in name_list_required:
            if not name_list_dict[name]:
                QMessageBox.critical(self, 'Ошибка', f'Заполните поле {name}!')
                flag_good = False
                break
        if flag_good:
            self.name_list_dict = name_list_dict
            self.configmaker.config_maker()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WgConfig()
    w.show()
    sys.exit(app.exec_())