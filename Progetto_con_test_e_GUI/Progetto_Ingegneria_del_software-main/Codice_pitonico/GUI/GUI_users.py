from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

#genero la finestra per il menù utenti
class domOS_users(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari
            self.utente_autenticato = None

            self.setWindowTitle("domOS")    #titolo
            self.resize(800, 600)           #dimensione
            self.setMinimumSize(600, 400)   #dimensione minima

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent                     #]---|questa parte qui si occupa di fetchare il percorso
            percorso_immagine = cartella_corrente / "schermatagenpurp_prot.png"     #    |dell'immagine che si vuole utilizzare come sfondo,
            percorso_str = str(percorso_immagine)                                   #    |(per motivi di compatibilità)
            self.pixmap_per_sfondo = QPixmap(percorso_str)                          #]---|

#---------------------------------------------------------------------------
#----------- GENERAZIONE PULSANTI, LISTE E CAMPI VARI PER LA GUI -----------
#---------------------------------------------------------------------------           
#le variabili click servono a contare quante volte un determinato pulsante
#viene premuto, per eseguire determinate azioni (es: mostrare e nascondere parti della gui)
#la variabile usoConferma serve a selezionare l'azione del pulsante conferma:
#siccome questo pulsante viene "riciclato", ovvero viene utilizzato lo stesso pulsante 
#associato alla stessa funzione in parti diverse di codice, usoConferma seleziona
#la funzione che il pulsante conferma dovrà svolgere.

            self.listaUsers = QListWidget(self)
            self.listaUsers.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaUsers.hide()
            self.click0 = 0

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

        #"nuovouser" si occupa di impostare il menù principale per la generazione di nuovi utenti
        #è una funzione puramente grafica
        def nuovouser(self):
            
            #al primo click di nuovo account:
            if self.click1 == 0:
                self.click0 = self.click2 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click1 = 1
                self.usoConferma = 0    #imposto usoConferma a 0 (per sicurezza, datochè di default è 0 ma potrebbe essere 1)
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]] #pulisco i campi
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]] #faccio comparire i campi
                self.btn1.show()    #mostro il pulsante conferma
                self.listaUsers.hide()  #nascondo la lista per evitare sovrapposizioni

            #al secondo click: 
            else:
                self.click1 = 0
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]#pulisco i campi
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]] #nascondo i campi
                self.btn1.hide()    #nascondo il pulsante conferma

        #"rimuoviuser" si occupa di impostare il menù principale per l'eliminazione di utenti
        #è una funzione puramente grafica 
        def rimuoviuser(self):
            
            #al primo click del pulsante rimuovi account:
            if self.click2 == 0:
                self.click1 = self.click0 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click2 = 1
                self.usoConferma = 1    #imposto usoConferma a 0 (per sicurezza)
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]    #pulisco i campi
                [campo.hide() for campo in [self.campo2, self.campo3]]  #nascondo campo 2 e 3 (datochè non servono)
                self.campo1.show()  #mostro campo 1
                self.btn1.show()    #mostro pulsante conferma
                self.listaUsers.hide()  #nascondo la lista per evitare sovrapposizioni

            #al secondo click
            else:
                self.click2 = 0
                self.campo1.clear() #pulisco campo 1
                self.campo1.hide()  #nascondo campo 1
                self.btn1.hide()    #nascondo il pulsante conferma
        
        #"listausers" si occupa di mostrare la lista degli utenti
        def listausers(self):
            
            #al primo click del pulsante lista utenti:
            if self.click0 == 0:
                self.click1 = self.click2 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = 0
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]] #nascondo i campi
                self.btn1.hide()    #nascondo il pulsante conferma

                id_ut = None    #imposto l'id utente a None poichè non è necessario per richiedere la lista utenti a boundary
                comando = "lista"   #imposto l'operazione che voglio eseguire a "lista" per richiedere la lista
                self.listaUsers.clear() #pulisco la lista
                lista_utenti = self.boundary_utenti.menu_utente(comando, id_ut) #prendo la lista da boundary utenti
                if not lista_utenti:    #se non ci sono utenti nel sistema
                    self.listaUsers.addItem("Nessun utente registrato.")    #alla lista viene aggiunta solo questa scritta
                    return
                self.listaUsers.addItem("ELENCO UTENTI REGISTRATI (ACCOUNT OSPITE):")
                self.listaUsers.addItem("-" * 40)
                #ciclo for che "spacchetta" la lista utenti e la scrive nella lista della GUI
                for utente in lista_utenti:
                    id_utente = utente.get("id", "N/D")
                    nome_utente = utente.get("nome", "Sconosciuto")
                    testo_riga = f"ID: {id_utente} - Nome: {nome_utente}"
                    self.listaUsers.addItem(testo_riga)
                self.listaUsers.show()  #al termine dello spacchettamento, mostro la lista
                self.listaUsers.raise_()    #e la porto in alto per farla apparire su schermo

            #al secondo click:
            else:
                self.click0 = 1
                self.listaUsers.clear() #svuoto la lista
                self.listaUsers.hide()  #nascondo la lista

        #"indietro" riporta l'utente al menù principale della gui
        def indietro(self):

            from GUI.GUI_mainMenu import domOS_mainmenu
            self.finestra_menu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari)
            self.finestra_menu.show()
            self.close()

        #"conferma" è la funzione associata al tasto omonimo e può svolgere più azioni,
        #le quali dipendono dalla variabile usoConferma:
        def conferma(self):
            
            #quando usoConferma è 0, conferma si occupa della generazione di nuovi utenti
            #(come visto in precedenza, dove in "nuovouser" viene impostata a 0)
            if self.usoConferma == 0:

                from PyQt6.QtWidgets import QMessageBox #qmessagebox serve per la geenrazione di notifiche pop-up
                id_ut = self.campo1.text().strip()  
                nome = self.campo2.text().strip()
                pswd = self.campo3.text().strip()
                #prendo id, nome e password dai campi
                #controllo: l'id deve essere un numero intero positivo
                self.check_id = False

                if not self.check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        self.check_id = True
                    except ValueError:
                        #se non lo è, mostro un warning
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                
                #controllo: sono necessari id, nome e password
                if not id_ut or not nome or not pswd:
                    #se manca qualcosa, mostro un warning
                    QMessageBox.warning(
                    self, 
                    "Attenzione", 
                    "Tutti i campi sono obbligatori! Compila ID, Nome e Password."
                    )
                    return
                #passo id, nome e password al form registrazione dentro boundary utenti
                esito = self.boundary_utenti.form_registrazione(id_ut, nome, pswd)
    
                if esito == "Utente creato":
                    #se riesco a creare un account, mostro un info
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    "Registrazione completata con successo!"
                    )

                elif esito == "Utente già presente":
                    #se l'utente è già registrato nel sistema, mostro un warning
                    QMessageBox.warning(
                    self, 
                    "Errore Registrazione", 
                    "Attenzione: esiste già un account con questo ID!"
                    )

                else:
                    #per altri errori riguardo la registrazione, mostro un error
                    QMessageBox.critical(
                    self, 
                    "Errore", 
                    f"Impossibile completare l'operazione: {esito}"
                    )
                #una volta che ho registrato un nuovo utente, pulisco e nascondo i campi,
                #nascondo lista e pulsante conferma (per evitare glitch della gui) e 
                #azzero la variabile click1
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.listaUsers.hde()
                self.btn1.hide()
                self.click1 = 0

            #se invece usoConferma è 1, il pulsante conferma si occupa dell'eliminazione
            #di utenti dal sistema
            elif self.usoConferma == 1:
                
                from PyQt6.QtWidgets import QMessageBox #qmessagebox serve per la geenrazione di notifiche pop-up
                id_ut = self.campo1.text().strip() #prendo l'id da campo1
                comando = "elimina" #imposto il comando (che viene usato dentro boundary utenti) ad "elimina"
                #controllo: l'id deve essere intero positivo
                self.check_id = False   

                if not self.check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        self.check_id = True
                    except ValueError:
                        #se non lo è, mostro un warning
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return

                #passo a menu_utente dentro boundary utenti sia comando sia id
                feedback = self.boundary_utenti.menu_utente(comando, id_ut)
                if feedback == f"L'utente è stato eliminato":
                    #se l'eliminazione va a buon fine, mostro un info
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    f"L'account ID: {id_ut} è stato eliminato"
                    )
                    #e poi pulisco i campi, li nascondo e nascondo anche lista e pulsante conferma
                    #(nascondo lista per evitare glitch). Inoltre azzero click2
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.listaUsers.hide()
                    self.btn1.hide()
                    self.click2 = 0

                elif feedback == f"L'utente cercato non esiste":
                    #altrimenti, se l'utente non esiste mostro un warning
                    QMessageBox.critical(
                    self, 
                    "Errore", 
                    f"L'account ID: {id_ut} non esiste"
                    )
                    return
                
#---------------------------------------------------------------------------------------------------------------
#----------- FUNZIONE CHE SI OCCUPA DI RIDIMENSIONARE DINAMICAMENTE SFONDO, PULSANTI, LISTE E CAMPI ------------
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

            #prendo le dimensini della finestra
            larghezza = self.width()
            altezza = self.height()

            #di seguito ogni componente grafico viene ridimensionato porporzionalmente
            #ad altezza e larghezza correnti della finestra
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

            pulsantelMenu = (larghezza * 15) // 100
            pulsanteaMenu = (altezza * 5) // 100
            pulsantexMenu = int(((larghezza * 14.4) // 100) - 0.28*pulsantelMenu)
            pulsantey1Menu = int(((altezza * 26) // 100) + 1*pulsanteaMenu)
            pulsantey2Menu = int(((altezza * 26) // 100) + 2.5*pulsanteaMenu)
            pulsantey3Menu = int(((altezza * 26) // 100) + 4*pulsanteaMenu)
            pulsantey4Menu = int(((altezza * 26) // 100) + 8.5*pulsanteaMenu)

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
            self.btnIndietro.setGeometry(pulsantexMenu, pulsantey4Menu, pulsantelMenu, pulsanteaMenu)

            self.listaUsers.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)