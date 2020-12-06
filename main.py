from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow,
            QMessageBox, QLabel, qApp, QPushButton, QRadioButton,
            QSpinBox)
from PyQt5.QtCore import (QFile, Qt)
from PyQt5.QtGui import (QIcon, QPixmap)
from os.path import expanduser
from easysettings import EasySettings
import random, string , os, sys, pyperclip

try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'password.generator.python.program'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass

def resource_path(relative_path):
    """used by pyinstaller to see the relative path"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

pwgui = resource_path("./gui/main.ui")
pwlogo = resource_path("./gui/logo.png")
appbg = resource_path("./gui/app.png")
userfold = expanduser("~")
savedpw = EasySettings(userfold+"./saved.conf")


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        UIFile = QFile(pwgui)
        UIFile.open(QFile.ReadOnly)
        uic.loadUi(UIFile, self)
        UIFile.close()

        bgapp = QPixmap(appbg)
        self.bg.setPixmap(bgapp)

        #for pw gen
        Llet = string.ascii_lowercase
        Ulet = string.ascii_uppercase
        Spe = '+-!"#¤%&'
        Num = '0123456789'
        self.ranSym = Llet + Ulet + Spe + Num
        
        self.create.clicked.connect(self.cmdGeneratePassword)
        self.cppw.clicked.connect(self.cmdCopyPassword)
        self.savepw.clicked.connect(self.cmdSavePassword)
        self.savedpw.clicked.connect(self.cmdOpenPassword)
        self.savedpw.clicked.connect(self.cmdClear)

    def cmdOpenPassword(self):
        openfile = ("notepad.exe "+str(userfold)+"/saved.conf")
        os.system(openfile)
    
    def cmdCopyPassword(self):
        """copy the password in lineedit"""
        pyperclip.copy(self.passe.text())


    def cmdGeneratePassword(self):
        """generate password"""
        pwLen = self.lenpw.value()
        password = "".join(random.sample(self.ranSym, pwLen))
        self.passe.setText(password)

        
    def cmdClear(self):
        """clear content"""
        web = self.webe.clear()
        acc = self.acce.clear()
        psw = self.passe.clear() 


    def cmdSavePassword(self):
        """save the password to the easysettings conf file"""
        web = self.webe.text()
        acc = self.acce.text()
        psw = self.passe.text()
        savedpw.set(web+"-acc",acc)
        savedpw.set(web+"-pw",psw)
        savedpw.save()



style = '''
QPushButton, QLineEdit, QSpinBox {
    background-color: #eeeeee;
    selection-color: #eeeeee;
    border-color: #393E46;
    border: 2px;
    color: #393E46;
}
QLabel {
    color: #eeeeee;
}
QPushButton:hover,
QLineEdit:hover {
    color: #000000;
    background-color: #FFFFFF;
}  
QPushButton:pressed {
    color: #000000;
    background-color: #FFFFFF;
    border: 3px;
}  
'''


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(pwlogo))
app.setStyleSheet(style) 
window = GUI()
window.show()
app.exec_()