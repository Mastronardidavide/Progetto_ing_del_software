from datetime import datetime
import json
from PyQt6.QtWidgets import (QListWidget, QWidget, QVBoxLayout, QLabel, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

#genero la finestra per il menù principale
class domOS_mainmenu(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari

            self.setWindowTitle("domOS")    #titolo
            self.resize(800, 600)           #dimensione
            self.setMinimumSize(600, 400)   #dimensione minima

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent                     #]---|questa parte qui si occupa di fetchare il percorso
            percorso_immagine = cartella_corrente / "schermatagenpurp_prot.png"       #    |dell'immagine che si vuole utilizzare come sfondo,
            percorso_str = str(percorso_immagine)                                   #    |(per motivi di compatibilità)
            self.pixmap_per_sfondo = QPixmap(percorso_str)                          #]---|

#---------------------------------------------------------------------------
#----------- GENERAZIONE PULSANTI, LISTE E CAMPI VARI PER LA GUI -----------
#---------------------------------------------------------------------------           
#le variabili click servono a contare quante volte un determinato pulsante
#viene premuto, per eseguire determinate azioni (es: mostrare e nascondere parti della gui)

            self.listaStato = QListWidget(self)
            self.listaStato.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaStato.hide()
            self.click = 0

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

#------------------------------------------------------------------------------------------
#----------- FUNZIONI CHE SI OCCUPANO DELL'INTERFACCIAMENTO TRA GUI E PROGRAMMA -----------
#------------------------------------------------------------------------------------------

        def mostraStato(self):  #funzione che si occupa di mostrare lo stato del sistema, overo l'ultimo backup salvato
            
            #l'if serve a far comparire e scomparire la lista
            #al primo click del pulsante lista, vengono eseguite le istruzioni dentro questo if
            if self.click == 0: 
                    
                    self.listaStato.clear() #pulisco la lista
                    backup_completo = self.boundary_disp.mostraStato()
                    
                    #se non esiste un backup
                    if not backup_completo:
                        self.listaStato.addItem("Nessun dato di backup disponibile.") #nella lista scrivo solo questo
                        return
                    #parsing sicuro di una stringa temporale
                    orario_grezzo = backup_completo.get("orario", "")
                    try:
                        dt = datetime.fromisoformat(orario_grezzo)  #provo a trasformarela stringa che contiene data e orario in oggetto data/ora
                        data_formattata = dt.strftime("%d/%m/%Y alle ore %H:%M:%S") #se ci riesco, "decoro" l'oggetto
                    except ValueError:
                        data_formattata = orario_grezzo #se non riesco a traformare la stringa aggiungerò alla lista semplicemente la stringa che contiene data e ora
                    self.listaStato.addItem(f"Backup del: {data_formattata}") #aggiungo l'oggetto 
                    self.listaStato.addItem("─" * 40) 
                    stringa_grezza = backup_completo["contenuto"]
                    stringa_json_valida = stringa_grezza.replace("'", '"').replace("False", "false").replace("True", "true")
                    lista_dispositivi = json.loads(stringa_json_valida)
                    
                    #questa parte "spacchetta" il backup per caricare tutto nella lista
                    for disp in lista_dispositivi:
                        if disp["tipo"] == "attuatore":
                            orario_att = disp.get("orarioAttivazione", "Non specificato")
                            testo_riga = f"A: ID: [{disp['id']}], Nome: {disp['nome']} - Orario: {orario_att } - Stato: {disp['statoAttuatore']}"
                        else:
                            testo_riga = f"S: ID: [{disp['id']}], Nome: {disp['nome']} - Soglia: {disp['soglia']}"
                        self.listaStato.addItem(testo_riga)
                    self.listaStato.show()      #mostro la lista
                    self.listaStato.raise_()    #la porto in cima
                    self.click = 1             #aumento il conteggio click

            else:   #al secondo click del pulsante lista:
                self.listaStato.clear() #pulisco la lista 
                self.listaStato.hide()  #nascondo la lista
                self.click = 0

        def mostraDisp(self):   #funzione che apre il menù dispositivi al click del pulsante dispositivi
            from GUI.GUI_devices import domOS_devices
            self.finestra_devices = domOS_devices(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_devices.show()
            self.close()

        def mostraUsers(self):  #funzione che apre il menù utenti al click del pulsante utenti
            from GUI.GUI_users import domOS_users
            self.finestra_users = domOS_users(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_users.show()
            self.close()
            
        def mostraZone(self):   #funzione che apre il menù zone al click del pulsante zone
            from GUI.GUI_zones import domOS_zones
            self.finestra_zones = domOS_zones(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_zones.show()
            self.close()

        def mostraScenari(self):    #funzione che apre il menù scenari al click del pulsante scenari
            from GUI.GUI_scenarios import domOS_scenarios
            self.finestra_scenarios = domOS_scenarios(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_scenarios.show()
            self.close()

        def esci(self): #funzione che esegue il logout al click del pulsante logout

            self.utente_autenticato = None
            from GUI.GUI_login import domOS_login
            self.finestra_login = domOS_login(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_login.show()
            self.close()

#---------------------------------------------------------------------------------------------------------------
#----------- FFUNZIONE CHE SI OCCUPA DI RIDIMENSIONARE DINAMICAMENTE SFONDO, PULSANTI, LISTE E CAMPI -----------
#---------------------------------------------------------------------------------------------------------------         
#ridimensionare dinamicamente nel senso che le dimensioni di tutti i componenti grafici sono proporzionali alla dimensione
#della finestra, perciò se la dimensione della finestra cambia, cambiano anche le dimensioni dei componenti grafici.
#Questo permette alla GUI di mantenere la sua organizzazione di default per qualsiasi dimensione scelta dall'utente

        def resizeEvent(self, event):
            
            #le 7 righe seguenti servono a scalare l'immagine di sfondo cercando di
            #mantenere la qualità originale, per poi assegnarla come sfondo.
            self.sfondo.resize(self.size())
            pixmap_scalata = self.pixmap_per_sfondo.scaled(
                self.size(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.sfondo.setPixmap(pixmap_scalata)
            
            #raccolgo larghezza ed altezza correnti della finestra
            larghezza = self.width()
            altezza = self.height()

            #di seguito ogni componente grafico viene ridimensionato porporzionalmente
            #ad altezza e larghezza correnti della finestra
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