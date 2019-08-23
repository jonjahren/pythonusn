####################################################
# Variabler får navn etter C-konvensjon.           #
# eks. om det er logisk med 2 ord så får vi en     #
# underscore: variable_name                        #
#                                                  #
# Løkker får en ny linje mellomrom ned til ny      #
# løkke.                                           #
#                                                  #
#                                                  #
####################################################

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit
import hangman_funksjoner as hmf

guess_word_output = ''.join(hmf.guess_word)

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
        
        
        ######################################################
        #                                                    #
        # Denne funksjonen er unødvendig lang, om vi hadde   #
        # hatt mer tid skulle denne blitt ryddet oppp        #
        # og debug-prints blitt fjernet                      #
        #                                                    #
        ######################################################
        
        def enter_press():
            print(hmf.random_word)
            enter_value = hangman.input_box.text()
            print(type(enter_value))
            hmf.input_letter = enter_value
            hmf.solve_index = hmf.find_placement(hmf.input_letter)
            print(hmf.solve_index)
            print(hmf.input_letter)
            hmf.check_input()
            hmf.solve_word()
            hangman.input_box.clear()
            used_letters_string = ''.join(hmf.used_letters)
            input_letter_show.setText(used_letters_string)
            guess_word_output = ''.join(hmf.guess_word)
            guess_word_show.setText(guess_word_output)
         
        ##########################################
        # Enkle knappe-definisjoner for hva      #
        # som skal skje når man trykker på       #
        # en knapp.                              #
        #                                        #
        ##########################################
        
        def knapp1_clicked():
            print(hmf.random_word)
        
        def knapp2_clicked():
            sys.exit()
        
        def knapp3_clicked():
            value = enter_press
            print(value)
        
        ##############################################
        #                                            #
        # QLabel er en funksjon for å printe tekst   #
        # til standard-vinduet som lages.            #
        #                                            #
        #                                            #
        ##############################################
        
        input_letter_show = QLabel(hangman)
        input_letter_show.setText(hmf.input_letter)
        input_letter_show.move(250, 400)
        input_letter_show.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
        input_letter_show.show()
        
        guess_word_show = QLabel(hangman)
        guess_word_show.setText(guess_word_output)
        guess_word_show.move(90, 400)
        guess_word_show.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
        guess_word_show.show()
            
        ##########################################
        #                                        #
        #                                        #
        # Setter opp trykk-knapper               #
        #                                        #
        ##########################################
        
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
        
        ########################################
        #                                      #
        # QLineEdit gir oss en tekst-boks som  #
        # vi kan skrive input i.               #
        # returnPressed.connect betyr at       #
        # funksjonen i parantes blir kjørt når #
        # man trykker enter.                   #
        #                                      #
        ########################################
        
        hangman.input_box = QLineEdit(hangman)
        hangman.nameLabel = QLabel(hangman)
        hangman.nameLabel.setText('Skriv inn bokstav:')
        hangman.input_box.setMaxLength(1)
        hangman.input_box.move(152, 460)
        hangman.input_box.resize(200, 32)
        hangman.nameLabel.move(32, 460)
        hangman.nameLabel.resize(200, 32)
        hangman.input_box.returnPressed.connect(enter_press)
        
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HangmanWindow()
    mainWin.show()
    sys.exit( app.exec_() )