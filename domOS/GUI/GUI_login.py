from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel, QListWidget
from PyQt6.QtWidgets import QApplication

#genero la finestra per la parte di login
class domOS_login(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari, notificheOld):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari
            self.utente_autenticato = None

            self.setWindowTitle("domOS")    #titolo finestra
            self.resize(800, 600)           #dimensione
            self.setMinimumSize(600, 400)   #ridimensionamento minimo finestra

            self.sfondo = QLabel(self)                                          
            cartella_corrente = Path(__file__).resolve().parent                     #]---|questa parte qui si occupa di fetchare il percorso
            percorso_immagine = cartella_corrente / "schermatalogin_prot.png"       #    |dell'immagine che si vuole utilizzare come sfondo,
            percorso_str = str(percorso_immagine)                                   #    |(per motivi di compatibilità)
            self.pixmap_per_sfondo = QPixmap(percorso_str)                          #]---|

#---------------------------------------------------------------------------
#----------- GENERAZIONE PULSANTI, LISTE E CAMPI VARI PER LA GUI -----------
#---------------------------------------------------------------------------           
            
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

#------------------------------------------------------------------------------------------
#----------- FUNZIONI CHE SI OCCUPANO DELL'INTERFACCIAMENTO TRA GUI E PROGRAMMA -----------
#------------------------------------------------------------------------------------------

        def raccoglidatiacc(self):  #funzione che si occupa del login
                
                #raccolgo id, nome e password dai campi
                id_ut = self.campoID.text().strip()
                nome = self.campoNome.text().strip()
                pswd = self.campoPass.text().strip()

                #controllo: l'id deve essere un numero intero positivo
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(id_ut) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        #se non lo è, mostro una message box di avviso
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                #controllo se sono stati compilati tutti i campi obbligatori
                if not id_ut or not nome or not pswd:
                    
                    #se manca qualcosa tra id, nome e password mostro un messagebox warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                    self, 
                    "Attenzione", 
                    "Tutti i campi sono obbligatori! Compila ID, Nome e Password."
                    )
                    return
                #passo id, nome e password al boundary utenti per il login e controllo il feedback dalla gui
                login = self.boundary_utenti.form_login(id_ut, nome, pswd)
                #se le credenziali sono valide passo alla finestra del menù principale e poi chiudo la finestra di login
                self.centroNote(login) #invio il risultato del login al centro notifiche
                if login:
                    from GUI.GUI_mainMenu import domOS_mainmenu
                    self.finestra_menu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
                    self.finestra_menu.show()
                    self.close()
                #altrimenti, mostro un message box di errore
                else:
                    self.utente_autenticato = None
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Credenziali non valide!")

        def raccoglidatireg(self):  #funzione che si occupa della registrazione
            #cole il login, raccolgo id, nome e password dai campi
            id_ut = self.campoID.text().strip()
            nome = self.campoNome.text().strip()
            pswd = self.campoPass.text().strip()
            #controllo che l'id sia intero positivo
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
            #se manca qualcosa (id, nome, password)
            if not id_ut or not nome or not pswd:
                #mostro un messagebox di avviso
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(
                self, 
                "Attenzione", 
                "Tutti i campi sono obbligatori! Compila ID, Nome e Password."
                )
                return
            #passo tutto alla boundary
            esito = self.boundary_utenti.form_registrazione(id_ut, nome, pswd)
            #controllo cosa mi ritorna la boundary
            self.centroNote(esito) #invio il risultato al centro notifiche
            if esito == "Utente creato":
                #se tutto va a buon fine, mostro un message box di informazione
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Registrazione completata con successo!"
                )
            
            elif esito == "Utente già presente":
                #se l'utente esiste già, mostro un messagrbox di warning
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(
                    self, 
                    "Errore Registrazione", 
                    "Attenzione: esiste già un account con questo ID!"
                )
            else:
                #per qualsiasi altro errore, mostro un messagebox contenente l'errore
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.critical(
                    self, 
                    "Errore", 
                    f"Impossibile completare l'operazione: {esito}"
                )

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
#----------- FUNZIONE CHE SI OCCUPA DI RIDIMENSIONARE DINAMICAMENTE SFONDO, PULSANTI, LISTE E CAMPI -----------
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
            
            centroNx = int((larghezza * 7.5) // 100)
            centroNy = int((altezza * 1.5) // 100)
            centroNl = int((larghezza * 84) // 100)
            centroNa = int((altezza * 10) // 100)
            
            self.centroNotifiche.setGeometry(centroNx, centroNy, centroNl, centroNa)

            self.campoID.setGeometry(campox, campoy1, campol, campoa)
            self.campoNome.setGeometry(campox, campoy2, campol, campoa)
            self.campoPass.setGeometry(campox, campoy3, campol, campoa)

            self.btnInvia.setGeometry(pulsantexLog, pulsantey1Log, pulsantelLog, pulsanteaLog)
            self.btnRegistra.setGeometry(pulsantexLog, pulsantey2Log, pulsantelLog, pulsanteaLog)

            super().resizeEvent(event)