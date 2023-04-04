from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QWidget, QListWidgetItem, QListWidget, QPushButton, QVBoxLayout
import sys
from XeLib import download
from os import system

def get_items(item):
    x = 'choco install'
    for i in item:
        if i != 'Hone':
            if i != 'EchoX':
                if i == 'Google Chrome':
                    x = x + ' googlechrome'
                elif i == 'Teams':
                    x = x + ' microsoft-teams'
                elif i == 'firefox':
                    x = x + ' firefox'
        else:
            if i == 'EchoX':
                download('https://github.com/UnLovedCookie/EchoX/releases/latest/download/EchoX.bat', 'EchoX.bat', 'EchoX')
            if i == 'Hone':
                download('https://github.com/auraside/HoneCtrl/releases/latest/download/HoneCtrl.Bat', 'HoneCTRL.bat', 'HoneCTRL')
    return(x)

def item_downloader(items):
    print(f'Running command {get_items(items)}')

class DarkModePalette:
    def __init__(self):
        self.primary_color = QColor(49, 53, 59)
        self.secondary_color = QColor(68, 71, 74)
        self.accent_color = QColor(0, 122, 255)
        self.text_color = QColor(255, 255, 255)

class MainWindow(QWidget):
    def __init__(self, list1, list2):
        super().__init__()
        
        # set dark mode palette
        palette = DarkModePalette()
        self.setStyleSheet(
            f"""
            background-color: {palette.primary_color.name()};
            color: {palette.text_color.name()};
            QListWidget {{background-color: {palette.secondary_color.name()}}}
            QListWidget::item:selected {{background-color: {palette.accent_color.name()}}}
            QPushButton {{background-color: {palette.secondary_color.name()}; color: {palette.text_color.name()}}}
            QPushButton:hover {{background-color: {palette.accent_color.name()}}}
            """
        )

        # create QListWidget for list1
        self.list_widget_1 = QListWidget(self)
        self.list_widget_1.setGeometry(50, 50, 200, 200)

        # populate list1
        for item in list1:
            list_item = QListWidgetItem(item)
            list_item.setFlags(list_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            list_item.setCheckState(Qt.CheckState.Unchecked)
            self.list_widget_1.addItem(list_item)

        # create QListWidget for list2
        self.list_widget_2 = QListWidget(self)
        self.list_widget_2.setGeometry(300, 50, 200, 200)

        # populate list2
        for item in list2:
            list_item = QListWidgetItem(item)
            list_item.setFlags(list_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            list_item.setCheckState(Qt.CheckState.Unchecked)
            self.list_widget_2.addItem(list_item)

        # create confirm button
        self.confirm_button = QPushButton('Confirm', self)
        self.confirm_button.setGeometry(50, 260, 100, 30)
        self.confirm_button.clicked.connect(self.confirm)

        # create everything button
        self.everything_button = QPushButton('Everything', self)
        self.everything_button.setGeometry(400, 260, 100, 30)
        self.everything_button.clicked.connect(self.everything)

        # create powershell button
        self.powershell_button = QPushButton('Chocolatey', self)
        self.powershell_button.setGeometry(400, 300, 100, 30)
        self.powershell_button.clicked.connect(self.run_powershell)

        # create exit button
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setGeometry(50, 300, 100, 30)
        self.exit_button.clicked.connect(self.exit_app)
        
        # create exit button
        self.exit_button = QPushButton('PWR Fix', self)
        self.exit_button.setGeometry(50, 340, 100, 30)
        self.exit_button.clicked.connect(self.power_fix)

        # show the window
        self.setGeometry(100, 100, 550, 400)
        self.setWindowTitle('WindowWizard')
        self.show()

    def confirm(self):
        checked_items = []
        for i in range(self.list_widget_1.count()):
            item = self.list_widget_1.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
        for i in range(self.list_widget_2.count()):
            item = self.list_widget_2.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
        
        item_downloader(checked_items)

    def everything(self):
        all_items = []
        for i in range(self.list_widget_1.count()):
            item = self.list_widget_1.item(i)
            all_items.append(item.text())
        for i in range(self.list_widget_2.count()):
            item = self.list_widget_2.item(i)
            all_items.append(item.text())
        item_downloader(all_items)

    def run_powershell(self):
        system('powershell Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))')

    def exit_app(self):
        sys.exit()

    def power_fix(self):
        system('PowerCfg /SETACVALUEINDEX SCHEME_CURRENT SUB_PROCESSOR IDLEDISABLE 000 && PowerCfg /SETACTIVE SCHEME_CURRENT')

if __name__ == '__main__':
    # configure the lists in the main.py script
    list1 = ['Google Chrome', 'Firefox', 'Teams']
    list2 = ['EchoX', 'Hone']

    # create the application and window
    app = QApplication(sys.argv)
    window = MainWindow(list1, list2)

    # execute the application
    sys.exit(app.exec())
