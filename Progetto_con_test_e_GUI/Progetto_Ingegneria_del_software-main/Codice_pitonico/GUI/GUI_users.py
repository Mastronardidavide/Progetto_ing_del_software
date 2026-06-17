from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

class domOS_users(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari
            self.utente_autenticato = None

            self.setWindowTitle("domOS")
            self.resize(800, 600)
            self.setMinimumSize(600, 400)

            self.listaUsers = QListWidget(self)
            self.listaUsers.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaUsers.hide()
            self.click0 = 0

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent
            percorso_immagine = cartella_corrente / "schermatamultipurpose_prot.png"
            percorso_str = str(percorso_immagine)
            self.pixmap_per_sfondo = QPixmap(percorso_str)

            self.campo1 = QLineEdit(self)
            self.campo1.setPlaceholderText("Inserisci ID")
            self.campo1.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo1.hide()
            
            self.campo2 = QLineEdit(self)
            self.campo2.setPlaceholderText("Inserisci Nome")
            self.campo2.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo2.hide()

            self.campo3 = QLineEdit(self)
            self.campo3.setPlaceholderText("Inserisci Password")
            self.campo3.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo3.hide()

            self.btn1 = QPushButton("Conferma", self)
            self.btn1.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btn1.hide()
            self.btn1.clicked.connect(self.conferma)
            self.usoConferma = 0

            self.btnLista = QPushButton("Lista Utenti", self)
            self.btnLista.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnLista.clicked.connect(self.listausers)

            self.btnAdd = QPushButton("Nuovo account", self)
            self.btnAdd.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnAdd.clicked.connect(self.nuovouser)
            self.click1 = 0

            self.btnRemove = QPushButton("Rimuovi Account", self)
            self.btnRemove.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnRemove.clicked.connect(self.rimuoviuser)
            self.click2 = 0

            self.btnIndietro = QPushButton("Indietro", self)
            self.btnIndietro.setStyleSheet("""
                background-color: #1f3d75;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnIndietro.clicked.connect(self.indietro)

        def nuovouser(self):
            
            if self.click1 == 0:
                if self.click0 == 1:
                    self.click0 = 0
                if self.click2 == 1:
                    self.click2 = 0
                self.click1 += 1
                self.usoConferma = 0
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.show()
                self.listaUsers.hide()

            else:
                self.click1 += 1
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()

            if self.click1 >= 2:
                self.click1 = 0

        def rimuoviuser(self):

            if self.click2 == 0:
                if self.click0 == 1:
                    self.click0 = 0
                if self.click1 == 1:
                    self.click1 = 0
                self.usoConferma = 1
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()
                self.click2 += 1
                self.campo1.clear()
                self.campo1.show()
                self.btn1.show()
                self.listaUsers.hide()

            else:
                self.click2 += 1
                self.campo1.clear()
                self.campo1.hide()
                self.btn1.hide()

            if self.click2 >= 2:
                self.click2 = 0

        def listausers(self):
            
            if self.click0 == 0:
                self.click0 += 1
                if self.click1 == 1:
                    self.click1 = 0
                if self.click2 == 1:
                    self.click2 = 0
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()
                id_ut = None
                comando = "lista"
                self.listaUsers.clear()
                lista_utenti = self.boundary_utenti.menu_utente(comando, id_ut)
                if not lista_utenti:
                    self.listaUsers.addItem("Nessun utente registrato.")
                    return
                self.listaUsers.addItem("ELENCO UTENTI REGISTRATI (ACCOUNT OSPITE):")
                self.listaUsers.addItem("-" * 40)
                for utente in lista_utenti:
                    id_utente = utente.get("id", "N/D")
                    nome_utente = utente.get("nome", "Sconosciuto")
                    testo_riga = f"ID: {id_utente} - Nome: {nome_utente}"
                    self.listaUsers.addItem(testo_riga)
                self.listaUsers.show()
                self.listaUsers.raise_()

            else:
                self.click0 += 1
                self.listaUsers.clear()
                self.listaUsers.hide()

            if self.click0 >= 2: 
                self.click0 = 0
        
        def indietro(self):

            from GUI.GUI_mainMenu import domOS_mainmenu
            self.finestra_menu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_menu.show()
            self.close()

        def conferma(self):

            if self.usoConferma == 0:

                from PyQt6.QtWidgets import QMessageBox
                id_ut = self.campo1.text().strip()
                nome = self.campo2.text().strip()
                pswd = self.campo3.text().strip()
                self.check_id = False

                if not self.check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        self.check_id = True
                    except ValueError:
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                    
                if not id_ut or not nome or not pswd:
                    QMessageBox.warning(
                    self, 
                    "Attenzione", 
                    "Tutti i campi sono obbligatori! Compila ID, Nome e Password."
                    )
                    return
                
                esito = self.boundary_utenti.form_registrazione(id_ut, nome, pswd)
    
                if esito == "Utente creato":
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    "Registrazione completata con successo!"
                    )
            
                elif esito == "Utente già presente":
                    QMessageBox.warning(
                    self, 
                    "Errore Registrazione", 
                    "Attenzione: esiste già un account con questo ID!"
                    )

                else:
                    QMessageBox.critical(
                    self, 
                    "Errore", 
                    f"Impossibile completare l'operazione: {esito}"
                    )
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.listaUsers.hde()
                self.btn1.hide()
                self.click1 = 0

            elif self.usoConferma == 1:
                
                from PyQt6.QtWidgets import QMessageBox
                id_ut = self.campo1.text().strip()
                comando = "elimina"
                self.check_id = False

                if not self.check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        self.check_id = True
                    except ValueError:
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
    
                feedback = self.boundary_utenti.menu_utente(comando, id_ut)
                if feedback == f"L'utente è stato eliminato":
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    f"L'account ID: {id_ut} è stato eliminato"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.listaUsers.hide()
                    self.btn1.hide()
                    self.click2 = 0

                elif feedback == f"L'utente cercato non esiste":
                    QMessageBox.critical(
                    self, 
                    "Errore", 
                    f"L'account ID: {id_ut} non esiste"
                    )
                    return
                
        def resizeEvent(self, event):
            
            self.sfondo.resize(self.size())
            pixmap_scalata = self.pixmap_per_sfondo.scaled(
                self.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.sfondo.setPixmap(pixmap_scalata)
            
            larghezza = self.width()
            altezza = self.height()
        
            campol = (larghezza * 26) // 100
            campoa = (altezza * 5) // 100
            campox = int(((larghezza * 62) // 100) - 0.35*campol)
            campoy1 = int(((altezza * 35) // 100) + 0.3*campoa)
            campoy2 = int(((altezza * 35) // 100) + 1.6*campoa)
            campoy3 = int(((altezza * 35) // 100) + 2.9*campoa)
        
            pulsantelLog = (larghezza * 15) // 100
            pulsanteaLog = (altezza * 5) // 100
            pulsantexLog = int(((larghezza * 62) // 100) - 0.28*pulsantelLog)
            pulsantey1Log = int(((altezza * 35) // 100) + 4.9*pulsanteaLog)
            pulsantey2Log = int(((altezza * 35) // 100) + 8.5*pulsanteaLog)

            pulsantelMenu = (larghezza * 15) // 100
            pulsanteaMenu = (altezza * 5) // 100
            pulsantexMenu = int(((larghezza * 14.4) // 100) - 0.28*pulsantelMenu)
            pulsantey1Menu = int(((altezza * 26) // 100) + 1*pulsanteaMenu)
            pulsantey2Menu = int(((altezza * 26) // 100) + 2.5*pulsanteaMenu)
            pulsantey3Menu = int(((altezza * 26) // 100) + 4*pulsanteaMenu)
            pulsantey4Menu = int(((altezza * 26) // 100) + 5.5*pulsanteaMenu)
            pulsantey6Menu = int(((altezza * 26) // 100) + 8.5*pulsanteaMenu)

            listaGenPurpx = int((larghezza * 40.5) // 100)
            listaGenPurpy = int((altezza * 14.7) // 100)
            listaGenPurpl = int((larghezza * 50) // 100)
            listaGenPurpa = int((altezza * 50) // 100)

            self.campo1.setGeometry(campox, campoy1, campol, campoa)
            self.campo2.setGeometry(campox, campoy2, campol, campoa)
            self.campo3.setGeometry(campox, campoy3, campol, campoa)

            self.btn1.setGeometry(pulsantexLog, pulsantey1Log, pulsantelLog, pulsanteaLog)

            self.btnLista.setGeometry(pulsantexMenu, pulsantey1Menu, pulsantelMenu, pulsanteaMenu)
            self.btnAdd.setGeometry(pulsantexMenu, pulsantey2Menu, pulsantelMenu, pulsanteaMenu)
            self.btnRemove.setGeometry(pulsantexMenu, pulsantey3Menu, pulsantelMenu, pulsanteaMenu)
            self.btnIndietro.setGeometry(pulsantexMenu, pulsantey6Menu, pulsantelMenu, pulsanteaMenu)

            self.listaUsers.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)