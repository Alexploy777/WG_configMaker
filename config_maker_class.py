import sys
from dataclasses import dataclass
from PyQt5.QtWidgets import QFileDialog, QApplication


# @dataclass
class ConfigMaker:
    def __init__(self, ui_window):
        self.ui_window = ui_window
        self.file_name = 'conf.conf'

    # # [Interface]
    # PrivateKey: str
    # Address: str
    # DNS: str
    # # [Peer]
    # PublicKey: str
    # AllowedIPs: str
    # Endpoint: str
    #
    # file_name: str

    # def __post_init__(ui_window, *args, **kwargs):
    #     ui_window = ui_window


    def config_maker(self):
        self.file_name = self.ui_window.lineEdit_config_name.text()
        self.config = (f'[Interface]\n'
                  f'PrivateKey = {self.ui_window.PrivateKey}\n'
                  f'Address = {self.ui_window.Address}\n'
                  f'DNS = {self.ui_window.DNS}\n'
                  f'\n'
                  f'[Peer]\n'
                  f'PublicKey = {self.ui_window.PublicKey}\n'
                  f'AllowedIPs = {self.ui_window.AllowedIPs}\n'
                  f'Endpoint = {self.ui_window.Endpoint}')
        print(self.config)
        self.config_to_file()

    def config_to_file(self):

        file_name_path, _ = QFileDialog.getSaveFileName(self.ui_window, caption="Сохраняем словарь", directory=self.file_name, filter="конфиг-файл (*.conf)")
        if file_name_path:
            with open(file_name_path, 'w', encoding='utf-8') as f:
                f.write(self.config)


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





