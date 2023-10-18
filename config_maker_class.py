import os
import sys
from dataclasses import dataclass
import configparser
from PyQt5.QtWidgets import QFileDialog, QApplication


# @dataclass
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

    def config_reader(self):
        self.config_obj = configparser.ConfigParser()
        file_name_path, _ = QFileDialog.getOpenFileName(self.ui_window, caption="Открываем конфигурацию", directory= '/', filter="конфиг-файл (*.conf)")
        file_name = os.path.basename(file_name_path).split('.')[0]
        print(file_name)
        try:
            self.config_obj.read(file_name_path, encoding="utf-8")
            self.ui_window.lineEdit_Config_name.setText(file_name)
            self.ui_window.lineEdit_PrivateKey.setText(self.config_obj.get('Interface', 'PrivateKey'))
            self.ui_window.lineEdit_Address.setText(self.config_obj.get('Interface', 'Address'))
            self.ui_window.lineEdit_DNS.setText(self.config_obj.get('Interface', 'DNS'))
            self.ui_window.lineEdit_PublicKey.setText(self.config_obj.get('Peer', 'PublicKey'))
            self.ui_window.lineEdit_AllowedIPs.setText(self.config_obj.get('Peer', 'AllowedIPs'))
            self.ui_window.lineEdit_Endpoint.setText(self.config_obj.get('Peer', 'Endpoint'))
        except:
            self.ui_window.statusBar.showMessage('Не могу прочитать файл!')

        # self.config.read(self.config_file_name, encoding="utf-8")
        # self.config_file_item = self.config.get(section, item)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # [Interface]
    PrivateKey = 'XfW1w+2ut8n0jj2T7Bocy0uqv61fdHpTaJHbxl5uPeQ='
    Address = '10.128.40.127/32, fd64:e20:68a3::287f/128'
    DNS = '10.128.0.1'
    # [Peer]
    PublicKey = 'sb61ho9MhaxhJd6WSrryVmknq0r6oHEW7PP5i4lzAgM='
    AllowedIPs = '0.0.0.0/1, 128.0.0.0/1, ::/1, 8000::/1'
    Endpoint = 'nl.gw.xeovo.com:51820'

    file_name = 'confWG.conf'

    conf = ConfigMaker(PrivateKey=PrivateKey, Address=Address, DNS=DNS, PublicKey=PublicKey, AllowedIPs=AllowedIPs, Endpoint=Endpoint, file_name=file_name)
    conf.config_maker()

    # sys.exit(app.exec_())





