import configparser
import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox


class ConfigMaker:
    def __init__(self, ui_window):
        self.ui_window = ui_window

    def config_maker(self):
        self.config_obj = configparser.ConfigParser()
        self.file_name = self.ui_window.name_list_dict['Config_name']
        self.config_obj.add_section('Interface')
        self.config_obj.set('Interface', 'PrivateKey', self.ui_window.name_list_dict['PrivateKey'])
        self.config_obj.set('Interface', 'Address', self.ui_window.name_list_dict['Address'])
        self.config_obj.set('Interface', 'DNS', self.ui_window.name_list_dict['DNS'])
        if self.ui_window.name_list_dict['MTU']:
            self.config_obj.set('Interface', 'MTU', self.ui_window.name_list_dict['MTU'])

        self.config_obj.add_section('Peer')
        self.config_obj.set('Peer', 'PublicKey', self.ui_window.name_list_dict['PublicKey'])
        self.config_obj.set('Peer', 'AllowedIPs', self.ui_window.name_list_dict['AllowedIPs'])
        self.config_obj.set('Peer', 'Endpoint', self.ui_window.name_list_dict['Endpoint'])
        self.config_writer()

    def config_writer(self):
        file_name_path, _ = QFileDialog.getSaveFileName(self.ui_window, caption="Сохраняем словарь", directory=self.file_name, filter="конфиг-файл (*.conf)")
        if file_name_path:
            with open(file_name_path, 'w', encoding='utf-8') as f:
                self.config_obj.write(f)
        self.ui_window.statusBar.setStyleSheet("color: rgb(0, 0, 255);")
        self.ui_window.statusBar.showMessage(file_name_path)

    def config_reader(self):
        self.config_obj = configparser.ConfigParser()
        file_name_path, _ = QFileDialog.getOpenFileName(self.ui_window, caption="Открываем конфигурацию", directory= '/', filter="конфиг-файл (*.conf)")
        file_name = os.path.basename(file_name_path).split('.')[0]
        self.ui_window.lineEdit_MTU.clear()
        try:
            self.config_obj.read(file_name_path, encoding="utf-8")
            self.ui_window.lineEdit_Config_name.setText(file_name)
            self.ui_window.lineEdit_PrivateKey.setText(self.config_obj.get('Interface', 'PrivateKey'))
            self.ui_window.lineEdit_Address.setText(self.config_obj.get('Interface', 'Address'))
            self.ui_window.lineEdit_DNS.setText(self.config_obj.get('Interface', 'DNS'))
            if self.config_obj.has_option('Interface', 'MTU'):
                self.ui_window.lineEdit_MTU.setText(self.config_obj.get('Interface', 'MTU'))

            self.ui_window.lineEdit_PublicKey.setText(self.config_obj.get('Peer', 'PublicKey'))
            self.ui_window.lineEdit_AllowedIPs.setText(self.config_obj.get('Peer', 'AllowedIPs'))
            self.ui_window.lineEdit_Endpoint.setText(self.config_obj.get('Peer', 'Endpoint'))
            self.ui_window.statusBar.setStyleSheet("color: rgb(0, 170, 0);")
            self.ui_window.statusBar.showMessage(file_name_path)

        except:
            if file_name:
                self.ui_window.statusBar.showMessage('Не могу прочитать файл!')
                self.ui_window.statusBar.setStyleSheet("color: rgb(255, 0, 0);")
                QMessageBox.critical(self.ui_window, 'Ошибка', 'Не могу прочитать файл!')


if __name__ == '__main__':
    pass
