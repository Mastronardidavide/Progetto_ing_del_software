from datetime import datetime
import json
from PyQt6.QtWidgets import (QListWidget, QWidget, QVBoxLayout, QLabel, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

class domOS_mainmenu(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari

            self.click = 0

            self.setWindowTitle("domOS")
            self.resize(800, 600)
            self.setMinimumSize(600, 400)
            layout = QVBoxLayout(self)

            self.listaStato = QListWidget(self)
            self.listaStato.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaStato.hide()

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent
            percorso_immagine = cartella_corrente / "schermatamultipurpose_prot.png"
            percorso_str = str(percorso_immagine)
            self.pixmap_per_sfondo = QPixmap(percorso_str)

            self.btnStato = QPushButton("Stato", self)
            self.btnStato.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnStato.clicked.connect(self.mostraStato)

            self.btnDisp = QPushButton("Dispositivi", self)
            self.btnDisp.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnDisp.clicked.connect(self.mostraDisp)

            self.btnUtenti = QPushButton("Utenti", self)
            self.btnUtenti.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnUtenti.clicked.connect(self.mostraUsers)

            self.btnZone = QPushButton("Zone", self)
            self.btnZone.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnZone.clicked.connect(self.mostraZone)

            self.btnScenari = QPushButton("Scenari", self)
            self.btnScenari.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnScenari.clicked.connect(self.mostraScenari)

            self.btnEsci = QPushButton("Logout", self)
            self.btnEsci.setStyleSheet("""
                background-color: #1f3d75;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnEsci.clicked.connect(self.esci)

        def mostraStato(self):

            if self.click == 0:
                    self.listaStato.clear()
                    backup_completo = self.boundary_disp.mostraStato()

                    if not backup_completo:
                        self.listaStato.addItem("Nessun dato di backup disponibile.")
                        return
                    orario_grezzo = backup_completo.get("orario", "")
                    try:
                        dt = datetime.fromisoformat(orario_grezzo)
                        data_formattata = dt.strftime("%d/%m/%Y alle ore %H:%M:%S")
                    except ValueError:
                        data_formattata = orario_grezzo 
                    self.listaStato.addItem(f"Backup del: {data_formattata}")
                    self.listaStato.addItem("─" * 40) 
                    stringa_grezza = backup_completo["contenuto"]
                    stringa_json_valida = stringa_grezza.replace("'", '"').replace("False", "false").replace("True", "true")
                    lista_dispositivi = json.loads(stringa_json_valida)
                    
                    for disp in lista_dispositivi:
                        if disp["tipo"] == "attuatore":
                            orario_att = disp.get("orarioAttivazione", "Non specificato")
                            testo_riga = f"A: ID: [{disp['id']}], Nome: {disp['nome']} - Orario: {orario_att } - Stato: {disp['statoAttuatore']}"
                        else:
                            testo_riga = f"S: ID: [{disp['id']}], Nome: {disp['nome']} - Soglia: {disp['soglia']}"
                        self.listaStato.addItem(testo_riga)
                    self.listaStato.show()
                    self.listaStato.raise_()
                    self.click += 1

            else:
                self.listaStato.clear()
                self.listaStato.hide()
                self.click += 1

            if self.click >= 2:
                self.click = 0

        def mostraDisp(self):
            from GUI.GUI_devices import domOS_devices
            self.finestra_devices = domOS_devices(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_devices.show()
            self.close()

        def mostraUsers(self):
            from GUI.GUI_users import domOS_users
            self.finestra_users = domOS_users(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_users.show()
            self.close()
            
        def mostraZone(self):
            from GUI.GUI_zones import domOS_zones
            self.finestra_zones = domOS_zones(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_zones.show()
            self.close()

        def mostraScenari(self):
            from GUI.GUI_scenarios import domOS_scenarios
            self.finestra_scenarios = domOS_scenarios(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_scenarios.show()
            self.close()
        def esci(self):

            self.utente_autenticato = None
            from GUI.GUI_login import domOS_login
            self.finestra_login = domOS_login(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_login.show()
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

            pulsantelMenu = (larghezza * 15) // 100
            pulsanteaMenu = (altezza * 5) // 100
            pulsantexMenu = int(((larghezza * 14.4) // 100) - 0.28*pulsantelMenu)
            pulsantey1Menu = int(((altezza * 26) // 100) + 1*pulsanteaMenu)
            pulsantey2Menu = int(((altezza * 26) // 100) + 2.5*pulsanteaMenu)
            pulsantey3Menu = int(((altezza * 26) // 100) + 4*pulsanteaMenu)
            pulsantey4Menu = int(((altezza * 26) // 100) + 5.5*pulsanteaMenu)
            pulsantey5Menu = int(((altezza * 26) // 100) + 7*pulsanteaMenu)
            pulsantey6Menu = int(((altezza * 26) // 100) + 8.5*pulsanteaMenu)

            listaGenPurpx = int((larghezza * 40.5) // 100)
            listaGenPurpy = int((altezza * 14.7) // 100)
            listaGenPurpl = int((larghezza * 50) // 100)
            listaGenPurpa = int((altezza * 50) // 100)

            self.btnStato.setGeometry(pulsantexMenu, pulsantey1Menu, pulsantelMenu, pulsanteaMenu)
            self.btnDisp.setGeometry(pulsantexMenu, pulsantey2Menu, pulsantelMenu, pulsanteaMenu)
            self.btnUtenti.setGeometry(pulsantexMenu, pulsantey3Menu, pulsantelMenu, pulsanteaMenu)
            self.btnZone.setGeometry(pulsantexMenu, pulsantey4Menu, pulsantelMenu, pulsanteaMenu)
            self.btnScenari.setGeometry(pulsantexMenu, pulsantey5Menu, pulsantelMenu, pulsanteaMenu)
            self.btnEsci.setGeometry(pulsantexMenu, pulsantey6Menu, pulsantelMenu, pulsanteaMenu)

            self.listaStato.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)