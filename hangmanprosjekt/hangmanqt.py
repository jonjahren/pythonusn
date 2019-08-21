# https://pythonprogramminglanguage.com/pyqt5-hello-world/
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize    

class HelloWindow(QMainWindow):
    def __init__(hangman):
        QMainWindow.__init__(hangman)

        hangman.setMinimumSize(QSize(640, 480))    
        hangman.setWindowTitle("Hangman v0.1b") 

        centralWidget = QWidget(hangman)          
        hangman.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(hangman)     
        centralWidget.setLayout(gridLayout)  

        title = QLabel("Velkommen til Jon og Martins hangman", hangman) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)
        
        def knapp1_clicked():
            print("Knapp1 trykket")
        def knapp2_clicked():
            print("Knapp 2 trykket")
            
        knapp1 = QPushButton(hangman)
        knapp1.setText("Knapp1")
        knapp1.move(64,32)
        knapp1.clicked.connect(knapp1_clicked)
        
        knapp2 = QPushButton(hangman)
        knapp2.setText("Knapp2")
        knapp2.move(64,64)
        knapp2.clicked.connect(knapp2_clicked)
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )