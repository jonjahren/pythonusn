import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QTextBrowser
from hangman_funksjoner import *    

guess_word_output = ''.join(guess_word)

class HangmanWindow(QMainWindow):
    def __init__(hangman):
        QMainWindow.__init__(hangman)

        hangman.setMinimumSize(QSize(800, 600))    
        hangman.setWindowTitle("Hangman v0.1a") 

        centralWidget = QWidget(hangman)          
        hangman.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(hangman)     
        centralWidget.setLayout(gridLayout)

        title = QLabel("Velkommen til Jon og Martins hangman", hangman) 
        title.setAlignment(QtCore.Qt.AlignTop)
        title.setAlignment(QtCore.Qt.AlignHCenter)
        gridLayout.addWidget(title, 0, 0)
        
        guess_word_show = QLabel(hangman)
        guess_word_show.setText(guess_word_output)
        guess_word_show.move(700, 350)
        guess_word_show.show()
        
        def knapp1_clicked():
            print(random_word)
        
        def knapp2_clicked():
            sys.exit()
        
        def knapp3_clicked():
            print(find_placement(hangman.input_box.text))
        
        def enter_press():
            find_placement(hangman.input_box.text)
            
        knapp1 = QPushButton(hangman)
        knapp1.setText("Skriv inn løsningsord")
        knapp1.move(150, 520)
        knapp1.resize(220, 30)
        knapp1.clicked.connect(knapp1_clicked)
        
        knapp2 = QPushButton(hangman)
        knapp2.setText("Avslutt spill")
        knapp2.move(32, 520)
        knapp2.clicked.connect(knapp2_clicked)
        
        knapp3 = QPushButton(hangman)
        knapp3.setText("Nytt spill")
        knapp3.move(380, 520)
        knapp3.clicked.connect(knapp3_clicked)
        
        hangman.input_box = QLineEdit(hangman)
        hangman.nameLabel = QLabel(hangman)
        hangman.nameLabel.setText('Skriv inn bokstav:')
        hangman.input_box.setMaxLength(1)
        hangman.input_box.move(152, 460)
        hangman.input_box.resize(200, 32)
        hangman.nameLabel.move(32, 460)
        hangman.nameLabel.resize(200, 32)
        hangman.input_box.editingFinished.connect(enter_press)
        
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HangmanWindow()
    mainWin.show()
    sys.exit( app.exec_() )