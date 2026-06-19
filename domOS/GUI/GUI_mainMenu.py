from datetime import datetime
import json
from PyQt6.QtWidgets import (QListWidget, QWidget, QVBoxLayout, QLabel, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

#genero la finestra per il menù principale
class domOS_mainmenu(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari, notificheOld):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari

            self.setWindowTitle("domOS")    #titolo
            self.resize(800, 600)           #dimensione
            self.setMinimumSize(600, 400)   #dimensione minima

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent                            #]---|questa parte qui si occupa di fetchare il percorso
            percorso_immagine = cartella_corrente / "schermatamultipurpose_prot.png"       #    |dell'immagine che si vuole utilizzare come sfondo,
            percorso_str = str(percorso_immagine)                                          #    |(per motivi di compatibilità)
            self.pixmap_per_sfondo = QPixmap(percorso_str)                                 #]---|

#---------------------------------------------------------------------------
#----------- GENERAZIONE PULSANTI, LISTE E CAMPI VARI PER LA GUI -----------
#---------------------------------------------------------------------------           
#le variabili click servono a contare quante volte un determinato pulsante
#viene premuto, per eseguire determinate azioni (es: mostrare e nascondere parti della gui)

            self.centroNotifiche = QListWidget(self)
            self.centroNotifiche.setStyleSheet("""
                background-color: #0045b5;
                border: 2px solid #7a91b9;
                border-radius: 2px;
                color: white;
            """)
            self.centroNotifiche.show()
            self.centroNotifiche.raise_()
            self.centroNotifiche.clear()
            self.notifiche = notificheOld
            for n in self.notifiche:
                self.centroNotifiche.addItem(str(n))
            self.boundary_disp.notificaAtt.connect(self.centroNote)     #--|collego le notifiche da boundary disp,
            self.boundary_disp.notificaSens.connect(self.centroNote)    #  |prendo ciò che è stato inviato e lo
            self.boundary_disp.notificaAuto.connect(self.centroNote)    #--|passo alla funzione che si occupa dell centro notifiche

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
                    if not backup_completo:
                        self.listaStato.addItem("Nessun dato di backup disponibile.")
                        return

                    #recupero ed adattamento stringa data e orario
                    orario_grezzo = backup_completo.get("orario", "")
                    try:
                        dt = datetime.fromisoformat(orario_grezzo)
                        data_formattata = dt.strftime("%d/%m/%Y alle ore %H:%M:%S")
                    except ValueError:
                        data_formattata = orario_grezzo

                    self.listaStato.addItem(f"Backup del: {data_formattata}")
                    self.listaStato.addItem("─" * 40)

                    #"spacchetto" il contenuto
                    stringa_grezza = backup_completo.get("contenuto", "[]")

                    try:
                    #se la stringa esterna contiene una stringa interna JSON
                        primo_livello = json.loads(stringa_grezza)
    
                    #se il risultato è ancora una stringa
                        if isinstance(primo_livello, str):
                            stringa_valida = primo_livello.replace("'", '"').replace("False", "false").replace("True", "true")
                            lista_dispositivi = json.loads(stringa_valida)
                        else:
                            lista_dispositivi = primo_livello
                    except (json.JSONDecodeError, AttributeError):
                    #se la stringa è malformata all'origine
                        stringa_valida = str(stringa_grezza).replace('"', '').replace("'", '"').replace("False", "false").replace("True", "true")
                        try:
                            lista_dispositivi = json.loads(stringa_valida)
                        except Exception:
                            lista_dispositivi = []
                            self.listaStato.addItem("Errore critico nella decodifica dei dispositivi.")

                    #carico tutto nella lista
                    for disp in lista_dispositivi:
                        id_disp = disp.get("id", "N/D")
                        nome_disp = disp.get("nome", "Sconosciuto")
                        tipo_disp = str(disp.get("tipo", "sconosciuto")).strip().lower()
    
                        if tipo_disp == "attuatore":
                            orario_att = disp.get("orarioAttivazione", "Non specificato")
                            stato_att = disp.get("statoAttuatore", "N/D")
                            testo_riga = f"A: ID: [{id_disp}], Nome: {nome_disp} - Orario: {orario_att} - Stato: {stato_att}"
                        elif tipo_disp == "sensore":
                            soglia_sens = disp.get("soglia", "N/D")
                            testo_riga = f"S: ID: [{id_disp}], Nome: {nome_disp} - Soglia: {soglia_sens}"
                        else:
                            testo_riga = f"DATO NON RICONOSCIUTO: ID: [{id_disp}], Nome: {nome_disp} (Tipo: {tipo_disp})"
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
            self.finestra_devices = domOS_devices(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
            self.finestra_devices.show()
            self.close()

        def mostraUsers(self):  #funzione che apre il menù utenti al click del pulsante utenti
            from GUI.GUI_users import domOS_users
            self.finestra_users = domOS_users(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
            self.finestra_users.show()
            self.close()
            
        def mostraZone(self):   #funzione che apre il menù zone al click del pulsante zone
            from GUI.GUI_zones import domOS_zones
            self.finestra_zones = domOS_zones(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
            self.finestra_zones.show()
            self.close()

        def mostraScenari(self):    #funzione che apre il menù scenari al click del pulsante scenari
            from GUI.GUI_scenarios import domOS_scenarios
            self.finestra_scenarios = domOS_scenarios(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
            self.finestra_scenarios.show()
            self.close()

        def esci(self): #funzione che esegue il logout al click del pulsante logout

            self.utente_autenticato = None
            from GUI.GUI_login import domOS_login
            self.finestra_login = domOS_login(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
            self.finestra_login.show()
            self.close()
        
        #funzione che si occupa del centro notifiche: se ci sono notifiche, le aggiungo sia al centro notifiche
        #sia alla lista "notifiche", che poi passo ad ogni finestra della GUI, per mantenere le notifiche sullo schermo.
        def centroNote(self, notifica=None):
            if notifica is not None:
                stringa_notifica = notifica
                self.centroNotifiche.addItem(str(stringa_notifica))
                self.notifiche.append(stringa_notifica)
                self.centroNotifiche.scrollToBottom()
        #funzione che scrolla in automatico verso il basso appena viene caricato con le notifiche meno recenti
        #il centro notifiche
        def showEvent(self, event):
            super().showEvent(event)
            if self.centroNotifiche.count() > 0:
                self.centroNotifiche.scrollToBottom()

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

            centroNx = int((larghezza * 7.5) // 100)
            centroNy = int((altezza * 1.5) // 100)
            centroNl = int((larghezza * 84) // 100)
            centroNa = int((altezza * 10) // 100)
            
            self.centroNotifiche.setGeometry(centroNx, centroNy, centroNl, centroNa)
            
            self.btnStato.setGeometry(pulsantexMenu, pulsantey1Menu, pulsantelMenu, pulsanteaMenu)
            self.btnDisp.setGeometry(pulsantexMenu, pulsantey2Menu, pulsantelMenu, pulsanteaMenu)
            self.btnUtenti.setGeometry(pulsantexMenu, pulsantey3Menu, pulsantelMenu, pulsanteaMenu)
            self.btnZone.setGeometry(pulsantexMenu, pulsantey4Menu, pulsantelMenu, pulsanteaMenu)
            self.btnScenari.setGeometry(pulsantexMenu, pulsantey5Menu, pulsantelMenu, pulsanteaMenu)
            self.btnEsci.setGeometry(pulsantexMenu, pulsantey6Menu, pulsantelMenu, pulsanteaMenu)

            self.listaStato.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)