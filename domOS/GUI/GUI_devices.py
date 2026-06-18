from datetime import datetime
from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

#genero la finestra per il menù dispositvi
class domOS_devices(QWidget): 
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
            cartella_corrente = Path(__file__).resolve().parent                             #]---|questa parte qui si occupa di fetchare il percorso
            percorso_immagine = cartella_corrente / "schermatamultipurpose_prot.png"        #    |dell'immagine che si vuole utilizzare come sfondo,
            percorso_str = str(percorso_immagine)                                           #    |(per motivi di compatibilità)
            self.pixmap_per_sfondo = QPixmap(percorso_str)                                  #]---|

#---------------------------------------------------------------------------
#----------- GENERAZIONE PULSANTI, LISTE E CAMPI VARI PER LA GUI -----------
#---------------------------------------------------------------------------           
#le variabili click servono a contare quante volte un determinato pulsante
#viene premuto, per eseguire determinate azioni (es: mostrare e nascondere parti della gui)
#la variabile usoConferma serve a selezionare l'azione del pulsante conferma:
#siccome questo pulsante viene "riciclato", ovvero viene utilizzato lo stesso pulsante 
#associato alla stessa funzione in parti diverse di codice, usoConferma seleziona
#la funzione che il pulsante conferma dovrà svolgere.

            self.centroNotifiche = QListWidget(self)
            self.centroNotifiche.setStyleSheet("""
                background-color: #0045b5;
                border: 2px solid #7a91b9;
                border-radius: 2px;
                color: white;
            """)
            self.centroNotifiche.show()
            self.centroNotifiche.raise_()
            self.inizializzazione = 0
            self.notifiche = notificheOld
            self.centroNote(None, 0)
            self.boundary_disp.notificaAtt.connect(self.centroNote)     #--|collego le notifiche da boundary disp,
            self.boundary_disp.notificaSens.connect(self.centroNote)    #  |prendo ciò che è stato inviato e lo
            self.boundary_disp.notificaAuto.connect(self.centroNote)    #--|passo alla funzione che si occupa dell centro notifiche

            self.listaDisp = QListWidget(self)
            self.listaDisp.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaDisp.hide()
            self.click0 = 0

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

        #"conferma" è la funzione associata al tasto omonimo e può svolgere più azioni,
        #le quali dipendono dalla variabile usoConferma:
        def conferma(self):
            
            #se usoConferma è 0, "conferma" si occupa della generazione di nuovi dispositivi
            if self.usoConferma == 0:

                #prendo id, tipo e nome dai campi
                self.id = self.campo1.text().strip()
                self.tipo = self.campo2.text().strip().lower()
                self.nomeDisp = self.campo3.text().strip()
                self.comando = "aggiungi"   #comando = "aggiungi" da passare alla boundary

                #controllo: l'id deve essere intero positivo
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(self.id) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        #se non lo è mostro un warning
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                
                #se come tipo è stato digitato "sensore"
                if self.tipo == "sensore":
                    self.usoConferma = 1 #imposto usoconferma a 1
                    #pulisco campo 1,2 e 3, nascondo 2 e 3 e rinomino 1
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo2, self.campo3]]
                    self.campo1.setPlaceholderText("Soglia Sensore (float)")

                #se come tipo è stato digitato "attuatore"
                elif self.tipo == "attuatore": 
                    self.usoConferma = 2    #imposto usoConferma a 2
                    #pulisco campo 1,2 e 3, nascondo 3 e rinomino 1 e 2
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.campo3.hide()
                    self.campo1.setPlaceholderText("Orario Attivazione (HH:MM)")
                    self.campo2.setPlaceholderText("Stato Iniziale (On/Off)")
                
                #per qualsiasi altro tipo
                else:
                    #mostro un error
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Tipo dispositivo non valido")

                self.soglia_valida = False
                orario_attivazione = None
                self.soglia = None

            #in questo caso stiamo aggiungendo un dispostivo di tipo "sensore"
            elif self.usoConferma == 1:
                
                #controllo:la soglia deve essere float
                if not self.soglia_valida:
                    try:
                        soglia_input = self.campo1.text().strip()
                        self.soglia = float(soglia_input)
                        self.soglia_valida = True

                    except ValueError:
                        #se non lo è mostro un warning
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato soglia non valido"
                        )
                        self.campo1.clear()
                        return
                
                #passo tutto a menu_disp dentro boundary dispositivi
                feedback = self.boundary_disp.menu_disp(self.comando, self.id, self.tipo , self.nomeDisp, self.soglia)
                self.centroNote(1, feedback) #invio il risultato al centro notifiche
                #resetto il menù e mostro un info che notifica del successo dell'operazione
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

            #in questo caso stiamo aggiungendo un attuatore
            elif self.usoConferma == 2:
                
                #controlliamo e assegnamo il valore corretto a "stato"
                stato_str = self.campo2.text().strip().lower()
                if stato_str == "on":
                    stato_iniziale = True
                elif stato_str == "off":
                    stato_iniziale = False
                else:
                    #se il valore è non ammesso, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Formato stato non valido"
                    )
                    return
                
                orario_str = self.campo1.text().strip() #prendo l'orario da campo 1
                #controllo: l'orario deve avere formato HH:MM
                self.check_orario = False
                if not self.check_orario:
                    try:
                        orario_attivazione = datetime.strptime(orario_str, "%H:%M").time() #converto str in time tramite strinf parse time
                        self.check_orario = True
                    except ValueError:
                        #se il formato è sbagliato, mostro un warning
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato orario non valido. Usa il formato HH:MM (es. 14:30)."
                        )
                        return
                #siccome stiamo aggiungendo un attuatore, imposto soglia a None, poi passo tutto a 
                #menu_disp dentro boundary dispositivi
                soglia = None
                feedback = self.boundary_disp.menu_disp(self.comando, self.id, self.tipo , self.nomeDisp, soglia, stato_iniziale, orario_attivazione)
                self.centroNote(1, feedback) #invio il risultato al centro notifiche
                #resetto il menù e mostro un info che notifica del successo dell'operazione
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
            
            #se usoConferma è 3, "conferma" si occupa della rimozione di dispositivi
            elif self.usoConferma == 3:
                #imposto comando su "rimuovi", che verrà poi passato alla boundary
                self.comando = "rimuovi"
                self.tipo = self.nomeDisp = None #imposto tipo e nome a None poichè non ci servono
                rimuovidisp = self.campo1.text().strip() #prendo l'id del dispositivo da rimuovere da campo 1

                #controllo: l'id deve essere intero positivo
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(rimuovidisp) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        #se non lo è, mostro un warning
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                
                #passo tutto alla boundary
                feedback = self.boundary_disp.menu_disp(self.comando, rimuovidisp, self.tipo , self.nomeDisp)
                self.centroNote(1, feedback) #invio il risultato al centro notifiche

                if feedback == f"Errore: Dispositivo {rimuovidisp} non trovato":
                    #se l'id non è associato a nesun dispositivo, mostro un error
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Dispositivo non trovato")
                    self.campo1.clear()
                    return
                elif feedback == f"Dispositivo {rimuovidisp} rimosso con successo":
                    #se invece riesco a rimuovere il dispositivo, mostro un info
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        f"Dispositivo {rimuovidisp} rimosso con successo"
                    )
                    self.click2 = 0
                #pulisco il menù
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo1.hide()
                self.btn1.hide()
            
            #se usoConferma è 4, "conferma" ha la funzione di modificare un dispositivo
            elif self.usoConferma == 4:

                #prendo l'id da campo 1
                self.id_disp = self.campo1.text().strip()
                self.usoConferma = 5 #imposto usoConferma a 5, che mi servirà più avanti
                #controllo id: deve essere intero positivo
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(self.id_disp) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        #se non lo è, mostro un warning
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID deve essere un numero intero positivo."
                            )
                        return
                #dopodichè preparo il menù per raccogliere: soglia, stato iniziale e orario.
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo1.setPlaceholderText("Nuova Soglia")
                self.campo2.setPlaceholderText("Nuovo Stato Iniziale(On/Off)")
                self.campo3.setPlaceholderText("Nuovo Orario (HH:MM)")
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]

            #adesso "conferma" avrà le seguenti funzioni
            elif self.usoConferma == 5:
                
                #prendo soglia da campo1
                soglia_input = self.campo1.text().strip()
                #controllo: soglia deve essere float
                nuova_soglia = float(soglia_input) if soglia_input else None
                if nuova_soglia == None:
                    #se non lo è, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Formato soglia non valido o vuota. La soglia non verrà modificata."
                    )
                #prendo stato da campo 2 e controllo che abbia una forma valida. Se si, assegno
                #il valore gusto di stato
                nuovo_stato = False
                stato_input = self.campo2.text().strip().lower()
                if stato_input == "on":
                    nuovo_stato = True
                elif stato_input == "off":
                    nuovo_stato = False
                else:
                    #se non ha una forma valida, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Formato stato non valido o vuoto. Lo stato non verrà modificato."
                    )
                #prendo orario da campo 3 e controllo che sia HH:MM
                nuovo_orario = None
                orario_input = self.campo3.text().strip()
                self.check_orario = False
                if not self.check_orario:
                    try:
                        nuovo_orario = datetime.strptime(orario_input, "%H:%M").time() #converto str in time tramite strinf parse time
                        self.check_orario = True
                    except ValueError:
                        #se non è HH:MM, mostro un warning
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato orario non valido o vuoto. L'orario non verrà modificato."
                        )
                #passo tutto a menu_disp dentro boundary dispositivi e prendo feedback
                self.comando = "configura"
                self.tipo = self.nomeDisp = None
                feedback = self.boundary_disp.menu_disp(self.comando, self.id_disp, self.tipo, self.nomeDisp, nuova_soglia, nuovo_stato, nuovo_orario)
                self.centroNote(1, feedback) #invio il risultato al centro notifiche
                if feedback == f"dispositivo non trovato":
                    #se l'id del dispositivo non è registrato nel sistema, mostro un error
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Dispositivo non trovato")
                    self.campo1.clear()
                    return
                else:
                    #altrimenti mostro un info e resetto il menù
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        "Dispositivo configurato con successo."
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.click3 = 0

        #funzione associata al pulsante "lista dispositivi": si occupa di 
        #mostrare e nascondere la lista dei dispositivi presenti nel sistema
        def lista(self):

                #al primo click del pulsante:
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btn1.hide()
                if self.click0 == 0:
                    self.click1 = self.click2 = self.click3 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                    self.listaDisp.clear()  #pulisco la lista

                    #prendo la lista dispositivi da boundary, la "spacchetto" e la carico sulal lista GUI
                    righe_dispositivi = self.boundary_disp._g_disp.lista()
                    if not righe_dispositivi:
                        self.listaDisp.addItem("Nessun dispositivo presente nel sistema.")
                    else:
                        self.listaDisp.addItems(righe_dispositivi)
                    #mostro la lista e la porto in cima
                    self.listaDisp.show()
                    self.listaDisp.raise_()
                    self.click0 = 1

                #al secondo click: pulisco la lista e la nascondo
                else:
                    self.listaDisp.clear()
                    self.listaDisp.hide()
                    self.click0 = 0

        #"aggiungiDisp" si occupa di impostare il menù principale per l'aggiunta di dispositivi
        #è una funzione puramente grafica
        def aggiungiDisp(self):
                
                #al primo click del pulsante "aggiungi dispositivo":
                if self.click1 == 0:
                    self.click0 = self.click2 = self.click3 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                    self.usoConferma = 0 #imposto usoConferma a 0 per modificare il funzionamento dl pulsante "conferma"
                    self.listaDisp.hide() #nascondo la lista dispositivi per lo stesso motivo
                    #modifico il nome dei campi
                    self.campo1.setPlaceholderText("ID Dispositivo")
                    self.campo2.setPlaceholderText("Tipo Dispositivo")
                    self.campo3.setPlaceholderText("Nome Dispositivo")
                    #li pulisco e li mostro
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                    #mostro anche il pulsante "conferma"
                    self.btn1.show()
                    self.click1 = 1

                #al secondo click del pulsante "aggiungi dispositivo":
                else:
                    #nascondo campi e pulsante conferma
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.click1 = 0

        #"rimuoviDisp" si occupa di impostare il menù principale per la rimozione di dispositivi
        #è una funzione puramente grafica
        def rimuoviDisp(self):

                #al primo click del pulsante "rimuovi dispositivo":
                if self.click2 == 0:
                    self.click1 = self.click0 = self.click3 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                    self.usoConferma = 3    #imposto usoConferma a 3 per modificare il funzionamento dl pulsante "conferma"
                    self.listaDisp.hide()   #nascondo la lista dispositivi per lo stesso motivo
                    #pulisco i campi
                    #modifico il nome del campo 1, gli altri 2 non servono
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo2, self.campo3]]
                    self.campo1.setPlaceholderText("ID Dispositivo da eliminare") #cambio il suo nomes
                    self.campo1.show() #mostro campo 1
                    self.btn1.show() #mostro anche il pulsante "conferma"
                    self.click2 = 1
                
                #al secondo click del pulsante "rimuovi dispositivo":
                else :
                    #nascondo campi e pulsante conferma
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.listaDisp.hide()
                    self.click2 = 0 

        #"modificaDisp" si occupa di impostare il menù principale per la modifica dei parametri di dispositivi
        #è una funzione puramente grafica
        def modificaDisp(self):
                
                #al primo click del pulsante "rimuovi dispositivo":
                if self.click3 == 0:
                    self.click1 = self.click2 = self.click0 = 0 #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                    self.usoConferma = 4    #imposto usoConferma a 3 per modificare il funzionamento dl pulsante "conferma"
                    self.listaDisp.hide()   #nascondo la lista dispositivi per lo stesso motivo
                    #pulisco i campi
                    #modifico il nome del campo 1, gli altri 2 non servono
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo2, self.campo3]]
                    self.campo1.setPlaceholderText("ID Dispositivo da configurare")
                    self.campo1.show()  #mostro campo 1
                    self.btn1.show()    #mostro anche il pulsante "conferma"
                    self.click3 = 1

                #al secondo click del pulsante "rimuovi dispositivo":  
                else:
                    #nascondo campi e pulsante conferma
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btn1.hide()
                    self.listaDisp.hide()
                    self.click3 = 0

        #"indietro" riporta l'utente al menù principale della gui
        def indietro(self):

            from GUI.GUI_mainMenu import domOS_mainmenu
            self.finestra_mainmenu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_zone, self.boundary_scenari, self.notifiche)
            self.finestra_mainmenu.show()
            self.close()

        #funzione che si occupa del centro notifiche: se ci sono notifiche, le aggiungo sia al centro notifiche
        #sia alla lista "notifiche", che poi passo ad ogni finestra della GUI, per mantenere le notifiche sullo schermo.
        def centroNote(self, notifica=None, inizializzazione=None):
            #inizializzazione serve per aggiornare il centro ogni volta che viene aperta una nuova finestra GUI
            if inizializzazione == 0:
                self.centroNotifiche.clear()
                for n in self.notifiche:
                    self.centroNotifiche.addItem(str(n))
            elif notifica is not None:
                stringa_notifica = str(notifica)
                self.centroNotifiche.addItem(stringa_notifica)
                self.notifiche.append(stringa_notifica)
                self.centroNotifiche.scrollToBottom()

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

            centroNx = int((larghezza * 7.5) // 100)
            centroNy = int((altezza * 1.5) // 100)
            centroNl = int((larghezza * 84) // 100)
            centroNa = int((altezza * 10) // 100)
            
            self.centroNotifiche.setGeometry(centroNx, centroNy, centroNl, centroNa)

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