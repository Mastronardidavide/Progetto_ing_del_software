from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

class domOS_login(QWidget): 
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

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent
            percorso_immagine = cartella_corrente / "schermatalogin_prot.png"
            percorso_str = str(percorso_immagine)
            self.pixmap_per_sfondo = QPixmap(percorso_str)

            self.campoID = QLineEdit(self)
            self.campoID.setPlaceholderText("Inserisci il tuo ID")
            self.campoID.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            
            self.campoNome = QLineEdit(self)
            self.campoNome.setPlaceholderText("Inserisci il tuo Nome")
            self.campoNome.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)

            self.campoPass = QLineEdit(self)
            self.campoPass.setPlaceholderText("Inserisci la tua Password")
            self.campoPass.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)

            self.btnInvia = QPushButton("Accedi", self)
            self.btnInvia.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnInvia.clicked.connect(self.raccoglidatiacc)

            self.btnRegistra = QPushButton("Nuovo Utente", self)
            self.btnRegistra.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnRegistra.clicked.connect(self.raccoglidatireg)

        def raccoglidatiacc(self):
                
                id_ut = self.campoID.text().strip()
                nome = self.campoNome.text().strip()
                pswd = self.campoPass.text().strip()
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
    
                if not id_ut or not nome or not pswd:
    
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                    self, 
                    "Attenzione", 
                    "Tutti i campi sono obbligatori! Compila ID, Nome e Password."
                    )
                    return
        
                login = self.boundary_utenti.form_login(id_ut, nome, pswd)

                if login:
                    from GUI.GUI_mainMenu import domOS_mainmenu
                    self.finestra_menu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
                    self.finestra_menu.show()
                    self.close()

                else:
                    self.utente_autenticato = None
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Credenziali non valide!")

        def raccoglidatireg(self):
    
            id_ut = self.campoID.text().strip()
            nome = self.campoNome.text().strip()
            pswd = self.campoPass.text().strip()
            self.check_id = False
            
            if not self.check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        self.check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                
            if not id_ut or not nome or not pswd:
    
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(
                self, 
                "Attenzione", 
                "Tutti i campi sono obbligatori! Compila ID, Nome e Password."
                )
                return
            esito = self.boundary_utenti.form_registrazione(id_ut, nome, pswd)
        
            from PyQt6.QtWidgets import QMessageBox
        

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

            self.campoID.setGeometry(campox, campoy1, campol, campoa)
            self.campoNome.setGeometry(campox, campoy2, campol, campoa)
            self.campoPass.setGeometry(campox, campoy3, campol, campoa)

            self.btnInvia.setGeometry(pulsantexLog, pulsantey1Log, pulsantelLog, pulsanteaLog)
            self.btnRegistra.setGeometry(pulsantexLog, pulsantey2Log, pulsantelLog, pulsanteaLog)

            super().resizeEvent(event)