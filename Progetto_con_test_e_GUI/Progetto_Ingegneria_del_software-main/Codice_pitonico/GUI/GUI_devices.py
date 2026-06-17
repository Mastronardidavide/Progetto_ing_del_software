from datetime import datetime
from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

class domOS_devices(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari

            self.setWindowTitle("domOS")    #titolo
            self.resize(800, 600)           #dimensione
            self.setMinimumSize(600, 400)   #dimensione minima

            self.listaDisp = QListWidget(self)
            self.listaDisp.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaDisp.hide()
            self.click0 = 0

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent
            percorso_immagine = cartella_corrente / "schermatamultipurpose_prot.png"
            percorso_str = str(percorso_immagine)
            self.pixmap_per_sfondo = QPixmap(percorso_str)

            self.campo1 = QLineEdit(self)
            self.campo1.setPlaceholderText("Inserisci il tuo ID")
            self.campo1.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo1.hide()
            
            self.campo2 = QLineEdit(self)
            self.campo2.setPlaceholderText("Inserisci il tuo Nome")
            self.campo2.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo2.hide()

            self.campo3 = QLineEdit(self)
            self.campo3.setPlaceholderText("Inserisci la tua Password")
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

            self.btnLista = QPushButton("Lista Dispositivi", self)
            self.btnLista.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnLista.clicked.connect(self.lista)

            self.btnAdd = QPushButton("Aggiungi Dispositivo", self)
            self.btnAdd.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnAdd.clicked.connect(self.aggiungiDisp)
            self.click1 = 0

            self.btnRemove = QPushButton("Rimuovi Dispositivo", self)
            self.btnRemove.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnRemove.clicked.connect(self.rimuoviDisp)
            self.click2 = 0

            self.btnEdit = QPushButton("Configura Dispositivo", self)
            self.btnEdit.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnEdit.clicked.connect(self.modificaDisp)
            self.click3 = 0

            self.btnIndietro = QPushButton("Indietro", self)
            self.btnIndietro.setStyleSheet("""
                background-color: #1f3d75;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnIndietro.clicked.connect(self.indietro)

        def conferma(self):
            
            if self.usoConferma == 0:

                self.id = self.campo1.text().strip()
                self.tipo = self.campo2.text().strip().lower()
                self.nomeDisp = self.campo3.text().strip()
                self.comando = "aggiungi"
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(self.id) 
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
                    
                if self.tipo == "sensore":
                    self.usoConferma = 2
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo2, self.campo3]]
                    self.campo1.setPlaceholderText("Soglia Sensore (float)")

                elif self.tipo == "attuatore":
                    self.usoConferma = 3
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.campo3.hide()
                    self.campo1.setPlaceholderText("Orario Attivazione (HH:MM)")
                    self.campo2.setPlaceholderText("Stato Iniziale (On/Off)")
                else:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Tipo dispositivo non valido")

                self.soglia_valida = False
                orario_attivazione = None
                self.soglia = None

            elif self.usoConferma == 2:

                if not self.soglia_valida:
                    try:
                        soglia_input = self.campo1.text().strip()
                        self.soglia = float(soglia_input)
                        self.soglia_valida = True

                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato soglia non valido"
                        )
                        self.campo1.clear()
                        return

                self.boundary_disp.menu_disp(self.comando, self.id, self.tipo , self.nomeDisp, self.soglia)

                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()

                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Sensore aggiunto con successo!"
                )
                self.click1 = 0

            elif self.usoConferma == 3:

                stato_str = self.campo2.text().strip().lower()
                if stato_str == "on":
                    stato_iniziale = True
                elif stato_str == "off":
                    stato_iniziale = False
                else:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Formato stato non valido"
                    )
                    return
                orario_str = self.campo1.text().strip()
                self.check_orario = False
                if not self.check_orario:
                    try:
                        orario_attivazione = datetime.strptime(orario_str, "%H:%M").time() #converto str in time tramite strinf parse time
                        self.check_orario = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato orario non valido. Usa il formato HH:MM (es. 14:30)."
                        )
                        return
                soglia = None
                self.boundary_disp.menu_disp(self.comando, self.id, self.tipo , self.nomeDisp, soglia, stato_iniziale, orario_attivazione)
                
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()

                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Attuatore aggiunto con successo!"
                )
                self.click1 = 0
                
            elif self.usoConferma == 4:
                self.comando = "rimuovi"
                self.tipo = self.nomeDisp = None
                rimuovidisp = self.campo1.text().strip()
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(rimuovidisp) 
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
                
                feedback = self.boundary_disp.menu_disp(self.comando, rimuovidisp, self.tipo , self.nomeDisp)
                print(feedback)
                if feedback == f"Errore: Dispositivo {rimuovidisp} non trovato":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Dispositivo non trovato")
                    self.campo1.clear()
                    return
                elif feedback == f"Dispositivo {rimuovidisp} rimosso con successo":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        f"Dispositivo {rimuovidisp} rimosso con successo"
                    )
                    self.click2 = 0
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo1.hide()
                self.btn1.hide()
            
            elif self.usoConferma == 5:
                self.id_disp = self.campo1.text().strip()
                self.usoConferma = 6
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(self.id_disp) 
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
                    
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo1.setPlaceholderText("Nuova Soglia")
                self.campo2.setPlaceholderText("Nuovo Stato Iniziale(On/Off)")
                self.campo3.setPlaceholderText("Nuovo Orario (HH:MM)")
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]

            elif self.usoConferma == 6:
            
                soglia_input = self.campo1.text().strip()
                nuova_soglia = float(soglia_input) if soglia_input else None
                if nuova_soglia == None:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Formato soglia non valido o vuota. La soglia non verrà modificata."
                    )
                nuovo_stato = False
                stato_input = self.campo2.text().strip().lower()
                if stato_input == "on":
                    nuovo_stato = True
                elif stato_input == "off":
                    nuovo_stato = False
                else:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Formato stato non valido o vuoto. Lo stato non verrà modificato."
                    )
                nuovo_orario = None
                orario_input = self.campo3.text().strip()
                self.check_orario = False
                if not self.check_orario:
                    try:
                        nuovo_orario = datetime.strptime(orario_input, "%H:%M").time() #converto str in time tramite strinf parse time
                        self.check_orario = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato orario non valido o vuoto. L'orario non verrà modificato."
                        )
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Dispositivo configurato con successo."
                )
                self.comando = "configura"
                self.tipo = self.nomeDisp = None
                self.boundary_disp.menu_disp(self.comando, self.id_disp, self.tipo, self.nomeDisp, nuova_soglia, nuovo_stato, nuovo_orario)
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()
                self.click3 = 0

        def lista(self):

                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()
                if self.click0 % 2 == 0:
                    self.click1 = self.click2 = self.click3 = 0
                    self.listaDisp.clear()
                    righe_dispositivi = self.boundary_disp._g_disp.lista()
                    if not righe_dispositivi:
                        self.listaDisp.addItem("Nessun dispositivo presente nel sistema.")
                    else:
                        self.listaDisp.addItems(righe_dispositivi)
                    self.listaDisp.show()
                    self.listaDisp.raise_()
                    self.click0 += 1

                else:
                    self.listaDisp.clear()
                    self.listaDisp.hide()
                    self.click0 += 1

                if self.click0 >= 2:
                    self.click0 = 0

        def aggiungiDisp(self):
                
                if self.click1 % 2 == 0:
                    self.click0 = self.click2 = self.click3 = 0
                    self.listaDisp.hide()
                    self.campo1.setPlaceholderText("ID Dispositivo")
                    self.campo2.setPlaceholderText("Tipo Dispositivo")
                    self.campo3.setPlaceholderText("Nome Dispositivo")
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.listaDisp.hide()
                    self.btn1.setText("Conferma")
                    self.btn1.show()
                    self.click1 += 1

                else:
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.click1 += 1

                if self.click1 >= 2:
                    self.click1 = 0

        def rimuoviDisp(self):

                if self.click2 == 0:
                    self.click1 = self.click0 = self.click3 = 0
                    self.usoConferma = 4
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo2, self.campo3]]
                    self.listaDisp.hide()
                    self.campo1.setPlaceholderText("ID Dispositivo da eliminare")
                    self.btn1.setText("Conferma")
                    self.campo1.show()
                    self.btn1.show()
                    self.click2 += 1
                else :
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.listaDisp.hide()
                    self.click2 += 1 

                if self.click2 >= 2:
                    self.click2 = 0

        def modificaDisp(self):
                
                if self.click3 == 0:
                    self.click1 = self.click2 = self.click0 = 0
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo2, self.campo3]]
                    self.listaDisp.hide()
                    self.campo1.setPlaceholderText("ID Dispositivo da configurare")
                    self.btn1.setText("Conferma")
                    self.campo1.show()
                    self.btn1.show()
                    self.click3 += 1
                    
                else:
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.listaDisp.hide()
                    self.click3 += 1

                if self.click3 >= 2:
                    self.click3 = 0

        def indietro(self):
            from GUI.GUI_mainMenu import domOS_mainmenu
            self.finestra_mainmenu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_mainmenu.show()
            self.close()

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
            self.btnEdit.setGeometry(pulsantexMenu, pulsantey4Menu, pulsantelMenu, pulsanteaMenu)
            self.btnIndietro.setGeometry(pulsantexMenu, pulsantey6Menu, pulsantelMenu, pulsanteaMenu)

            self.listaDisp.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)