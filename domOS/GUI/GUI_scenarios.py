from datetime import datetime
from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

#genero la finestra per il menù zone
class domOS_scenarios(QWidget): 
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
            self.centroNotifiche.clear()
            self.notifiche = notificheOld
            for n in self.notifiche:
                self.centroNotifiche.addItem(str(n))
            self.boundary_disp.notificaAtt.connect(self.centroNote)     #--|collego le notifiche da boundary disp,
            self.boundary_disp.notificaSens.connect(self.centroNote)    #  |prendo ciò che è stato inviato e lo
            self.boundary_disp.notificaAuto.connect(self.centroNote)    #--|passo alla funzione che si occupa dell centro notifiche

            self.listaScen = QListWidget(self)
            self.listaScen.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaScen.hide()
            self.click0 = 0

            self.campo1 = QLineEdit(self)
            self.campo1.setPlaceholderText("")
            self.campo1.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo1.hide()
            
            self.campo2 = QLineEdit(self)
            self.campo2.setPlaceholderText("")
            self.campo2.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo2.hide()

            self.campo3 = QLineEdit(self)
            self.campo3.setPlaceholderText("")
            self.campo3.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
            """)
            self.campo3.hide()

            self.btnConferma = QPushButton("Conferma", self)
            self.btnConferma.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnConferma.hide()
            self.btnConferma.clicked.connect(self.conferma)
            self.usoConferma = 0

            self.btnLista = QPushButton("Lista Scenari", self)
            self.btnLista.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnLista.clicked.connect(self.lista)
            self.click0 = 0

            self.btnAdd = QPushButton("Aggiungi Scenario", self)
            self.btnAdd.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnAdd.clicked.connect(self.aggiungi)
            self.click1 = 0

            self.btnRemove = QPushButton("Rimuovi Scenario", self)
            self.btnRemove.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnRemove.clicked.connect(self.rimuovi)
            self.click2 = 0

            self.btnEdit = QPushButton("Rinomina Scenario", self)
            self.btnEdit.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnEdit.clicked.connect(self.rinomina)
            self.click3 = 0

            self.btnOra = QPushButton("Orario", self)
            self.btnOra.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnOra.clicked.connect(self.orario)
            self.click4 = 0

            self.btnAuto = QPushButton("Associa Sensore", self)
            self.btnAuto.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnAuto.clicked.connect(self.associa_sens)
            self.click5 = 0

            self.btnAssocia = QPushButton("+/- Attuatore", self)
            self.btnAssocia.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnAssocia.clicked.connect(self.diss_associa_att)
            self.click6 = 0
            self.click7 = 0

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
            
            #se usoConferma è 0, il pulsante conferma si occupa della generazione di scenari
            if self.usoConferma == 0:
                
                #prendo i dati dai campi e imposto comando su "aggiungi" (da passare a boundary)
                id_scen = self.campo1.text().strip()
                nome_scen = self.campo2.text().strip()
                comando = "aggiungi"

                #check id: deve essere intero positivo
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(id_scen) 
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
                
                #passo tutti i dati alla boundary e prendo il feedback che mi restituisce
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome_scen)
                self.centroNote(feedback) #invio il risultato al centro notifiche

                from PyQt6.QtWidgets import QMessageBox
                #controllo il feedback
                if feedback == f"Lo scenario è già presente":
                    #se lo scenario è già presente, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "Lo scenario è già presente"
                    )
                    return
                else:
                    #se tutto va a buon fine, mostro un info e resetto il menù
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    "Scenario aggiunto con successo!"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()
                    self.click1 = 0

            #se usoConferma è 1, il pulsante conferma si occupa della rimozione di scenari
            elif self.usoConferma == 1:

                #prendo i dati dai campi
                id_scen = self.campo1.text().strip()
                comando = "rimuovi"
                #controllo id: deve essere intero positivo
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(id_scen) 
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
                
                #passo tutto a boundary e prendo il feedback
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen)
                self.centroNote(feedback) #invio il risultato al centro notifiche

                if feedback == f"Scenario eliminato":
                    #se l'eliminazione va a buon fine, mostro un info e resetto il menù
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        "Scenario eliminato con successo!"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()
                    self.click2 = 0

                elif feedback == f"Scenario non trovato":
                    #altrimenti, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
            
            #se usoConferma è 2, il pulsante conferma si occupa di modificare il nome degli scenari
            elif self.usoConferma == 2:
                
                #prendo tutti i dati dai campi
                id_edit = self.campo1.text().strip()
                nome_edit = self.campo2.text().strip()
                comando = "rinomina"

                #controllo id: deve essere intero positivo
                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_edit) 
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
                #passo tutto a boundary e prendo il feedback
                feedback = self.boundary_scenari.menu_scenari(comando, id_edit, nome_edit)
                self.centroNote(feedback) #invio il risultato al centro notifiche
                if feedback == f"Scenario non trovato":
                    #se lo scenario non è presente, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
                else: 
                    #se invece non ci sono errori, mostro un info e resetto il menù
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    "Nome Scenario modificato con successo!"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()
                    self.click3 = 0

            #se usoConferma è 3, il pulsante conferma si occupa di aggiungere orario di accensione e
            #spegnimento allo scenario
            elif self.usoConferma == 3:
                
                #prendo tutti i dati dai campi
                id_scen = self.campo1.text().strip()
                orario1 = self.campo2.text().strip()
                orario2 = self.campo3.text().strip()
                comando = "orario"
                
                #controllo id: deve essere intero positivo
                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_scen) 
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

                #controllo il formato dell'orario di accensione, che deve essere HH:MM
                self.check_orario = False
                if not self.check_orario:
                    try:
                        orario_on = datetime.strptime(orario1, "%H:%M").time() #converto str in time tramite strinf parse time
                        self.check_orario = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato orario attivazione non valido o non inserito. Usa il formato HH:MM (es. 14:30)."
                        )
                        return
                    
                #controllo il formato dell'orario di spegnimento, che deve essere HH:MM
                self.check_orario = False
                if not self.check_orario:
                    try:
                        orario_off = datetime.strptime(orario2, "%H:%M").time() #converto str in time tramite strinf parse time
                        self.check_orario = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato orario disattivazione non valido o non inserito. Usa il formato HH:MM (es. 14:30)."
                        )
                        return
                
                #passo tutto a boundary e prendo il feedback che mi restituisce, per il controllo
                nome = None
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off)
                self.centroNote(feedback) #invio il risultato al centro notifiche
                if feedback == f"Scenario non trovato":
                    #se l'id non è associato a nessuno scenario, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
                
                else:
                    #se invece non ci sono errori, mostro un info e resetto il menù
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                    self, 
                    "Successo", 
                    "Pianificazione scenario completata!"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()
                    self.click4 = 0

            #se usoConferma è 4, il pulsante conferma si occupa di aggiungere sensori allo scenario
            elif self.usoConferma == 4:
                
                #raccolgo tutti i dati dai campi
                id_scen = self.campo1.text().strip()
                id_sens = self.campo2.text().strip()
                soglia = self.campo3.text().strip()
                comando = "automazione"

                #controllo id scenario: deve essere intero positivo
                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_scen) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID Scenario deve essere un numero intero positivo."
                            )
                        return
                
                #controllo id sensore: deve essere intero positivo
                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_sens) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID Sensore deve essere un numero intero positivo."
                            )
                        return
                
                #controllo soglia: deve essere float
                check_soglia = False
                if not check_soglia:
                    try:
                        soglia_sens = float(soglia)
                        check_soglia = True

                        if not (0.0 <= soglia <= 100.0):
                            raise ValueError("Range non valido")
                        
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato soglia non valido"
                        )
                        return
                
                #passo tutto a boundary e controllo il feedback che mi restituisce
                nome = orario_on = orario_off = None
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off, id_sens, soglia_sens)
                self.centroNote(feedback) #invio il risultato al centro notifiche
                if feedback == f"Scenario non trovato":
                    #se l'id scenario non è valido, mostro un errore
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
                elif feedback == f"Errore: Il sensore con ID '{id_sens}' non esiste nella domotica. Automazione annullata.":
                    #se l'id sensore non è valido, mostro un errore
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Sensore non trovato")
                    return
                elif feedback == f"Errore: Sensore e Soglia devono essere inseriti insieme.":
                    #se manca uno tra id sensore e soglia, mostro un warning
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "ID Sensore e Soglia devono essere inseriti insieme."
                        )
                    return
                
                else:
                    #se invece non ci sono errrori, mostro un info e resetto il menù
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        "Sensore associato con successo!"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()
                    self.click5 = 0

            #se usoConferma è 5, il pulsante conferma si occupa di aggiungere e rimuovere attuatori allo scenario
            elif self.usoConferma == 5:
                
                #prendo tutti i dati dai campi
                id_scen = self.campo1.text().strip()
                id_att = self.campo2.text().strip()
                comando = "associa"
                
                #controllo id scenario: deve essere intero positivo
                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_scen) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID Scenario deve essere un numero intero positivo."
                            )
                        return
                
                #controllo id attuatore: deve essere intero positivo
                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_att) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID Sensore deve essere un numero intero positivo."
                            )
                        return
                
                #passo tutto a boundary e controllo il feedback che mi restituisce
                nome = orario_on = orario_off = id_sens = soglia_sens = None
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off, id_sens, soglia_sens, id_att)
                self.centroNote(feedback) #invio il risultato al centro notifiche
                #se l'attuatore è già associato allo scenario, una volta cliccato "conferma" il codice proseguirà all'interno di questo if
                if feedback == f"L'attuatore '{id_att}' è già associato a questo scenario":

                    if self.click7 == 0:
                        #al primo click, siccome l'attuatore è già associato, mostro un warning, 
                        #il quale avverte l'utente dell'errore e lo informa che, premendo una seconda
                        #volta il tasto "conferma", l'attuatore verrà rimosso a meno che non venga
                        #modificato il suo id
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'Attuatore è già associato allo scenario. Premere 'Conferma' per dissociarlo o modificare il campo ID."
                            )
                        self.click7 += 1
                        return
                    
                    if self.click7 == 1:

                        #al secondo click, se l'id rimane lo stesso, significa che l'utente vuole dissociare il 
                        #dispositivo dalla zona. Modifico il comando che da "associa" diventa "dissocia",
                        #dopodichè passo i dati a boundary e prendo il feedback che mi restituisce
                        comando = "dissocia"
                        feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off, id_sens, soglia_sens, id_att)
                        self.centroNote(feedback) #invio il risultato al centro notifiche
                        if feedback == f"Scenario non trovato":
                            #se l'id zona non è valido, mostro un errore
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.critical(self, "Errore", "Scenario non trovato")
                            return
                        elif feedback == f"Errore: L'attuatore con ID '{id_att}' non esiste nel sistema.":
                            #se l'id attuatore non è valido, mostro un errore
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.critical(self, "Errore", "Attuatore non trovato")
                            return
                        elif feedback == f"Attuatore '{id_att}' rimosso dallo scenario con successo":
                            #se non ci sono errori, mostro un info e resetto il menù
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.information(
                                self, 
                                "Successo", 
                                "Attuatore dissociato con successo!"
                            )
                            self.click7 = 0
                            self.click6 = 0
                            [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                            [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                            self.btnConferma.hide()

                #stessi controlli eseguiti sopra: sono scritti anche qui perchè, mentre sopra
                #i controlli vengono eseguiti per la rimozione di un attuatore, qui vengono
                #eseguiti per l'aggiunta di un attuatore.
                elif feedback == f"Scenario non trovato":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
                elif feedback == f"Errore: L'attuatore con ID '{id_att}' non esiste nel sistema.":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Attuatore non trovato")
                    return
                elif feedback == f"Attuatore '{id_att}' associato allo scenario con successo":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        "Attuatore associato con successo!"
                    )
                    self.click7 = 0
                    self.click6 = 0
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()

        #funzione associata al pulsante "lista scenari": si occupa di 
        #mostrare e nascondere la lista degli scenari presenti nel sistema
        def lista(self):
            
            #al primo click:
            if self.click0 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click1 = self.click4 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                #setup vari, sempre per evitare sovrapposizioni
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.listaScen.clear()  #pulisco la lista
                self.listaScen.addItem("Lista Zone presenti nel sistema") #"intitolo" la lista
                self.listaScen.addItem("_" * 40)
                lista_scenari = self.boundary_scenari.menu_scenari("lista") #raccolgo la lista effettiva degli scenari da boundary
                if not lista_scenari:
                    self.listaScen.addItem("Nessuna zona registrata nel sistema.") #se non ci sono scenari scrivo questo
                #se invece sono presenti scenari nel sistema, "spacchetto" la lista e aggiungo tutto alla lista GUI.
                for scenario_oggetto in lista_scenari:
                    scenario = scenario_oggetto.toDict()
                    id_scen = scenario.get("id", "N/D")
                    nome_scen = scenario.get("nome", "Sconosciuto")
                    orarioattivazione = scenario.get("orarioScenario", "N/D")
                    orariodisattivazione = scenario.get("orarioDisattivazione", "N/D")
                    sogliazona = scenario.get("sogliaScenario", "N/D")
                    id_sens = scenario.get("id_sensore", "N/D")
                    id_att = scenario.get("id_attuatori", [])
                    if not id_att:
                        attuatori_str = "None"
                    else:
                        attuatori_str = ", ".join(id_att)
                    riga_testo = (f"[ID: {id_scen}] - Scenario: {nome_scen}\n"
                                  f"Attivazione: {orarioattivazione} - Disattivazione: {orariodisattivazione} - Soglia: {sogliazona}\n"
                                  f"Sensore [ID]: {id_sens} - Attuatori [ID]: {attuatori_str}"  
                    )
                    self.listaScen.addItem(riga_testo)
                    self.listaScen.addItem("_" * 40)    #separo ogni scenario con _
                #alla fine mostro e metto in cima la lista
                self.listaScen.show()
                self.listaScen.raise_()
                self.click0 = 1

            #al secondo click, pulisco e nascondo la lista
            else:
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.listaScen.clear()
                self.listaScen.hide()
                self.click0 = 0
        
        #"aggiungi" si occupa di impostare il menù principale per l'aggiunta di scenari
        #è una funzione puramente grafica
        def aggiungi(self):

            #al primo click:
            if self.click1 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = self.click4 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 0 #imposto usoConferma a 0 per modificare il funzionamento dl pulsante "conferma"
                #preparo il menù: pulisco i campi che mi servono e ne modifico il nome, nascondo la lista
                #per evitare sovrapposizioni e mostro pulsante conferma e campi
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScen.hide()
                self.campo1.setPlaceholderText("ID Nuovo Scenario")
                self.campo2.setPlaceholderText("Nome Nuovo Scenario")
                [campo.show() for campo in [self.campo1, self.campo2]]
                self.btnConferma.show()
                self.click1 = 1
            
            #al secondo click, pulisco e nascondo i campi e nascondo anche il pulsante conferma
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click1 = 0
        
        #"rimuovi" si occupa di impostare il menù principale per la rimozione di scenari
        #è una funzione puramente grafica
        def rimuovi(self):
            
            #al primo click:
            if self.click2 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = self.click1 = self.click4 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 1 #imposto usoConferma a 1 per modificare il funzionamento dl pulsante "conferma"
                #preparo il menù: pulisco i campi che mi servono e ne modifico il nome, nascondo la lista
                #per evitare sovrapposizioni e mostro pulsante conferma e campi
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScen.hide()
                self.campo1.setPlaceholderText("ID Scenario da eliminare")
                self.campo1.show()
                self.btnConferma.show()
                self.click2 = 1

            #al secondo click, pulisco e nascondo i campi e nascondo anche il pulsante conferma
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click2 = 0

        #"rinomina" si occupa di impostare il menù principale per la modifica del nome di scenari
        #è una funzione puramente grafica
        def rinomina(self):

            #al primo click:
            if self.click3 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = self.click1 = self.click2 = self.click4 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 2 #imposto usoConferma a 2 per modificare il funzionamento dl pulsante "conferma"
                #preparo il menù: pulisco i campi che mi servono e ne modifico il nome, nascondo la lista
                #per evitare sovrapposizioni e mostro pulsante conferma e campi
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScen.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("Nuovo nome")
                [campo.show() for campo in [self.campo1, self.campo2]]
                self.btnConferma.show()
                self.click3 += 1
            #al secondo click, pulisco e nascondo i campi e nascondo anche il pulsante conferma
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click3 += 1

            if self.click3 >= 2:
                self.click3 = 0

        #"orario" si occupa di impostare il menù principale per l'aggiunta di orari per l'automazione
        #è una funzione puramente grafica
        def orario(self):
            
            #al primo click:
            if self.click4 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = self.click1 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 3 #imposto usoConferma a 2 per modificare il funzionamento dl pulsante "conferma"
                #preparo il menù: pulisco i campi che mi servono e ne modifico il nome, nascondo la lista
                #per evitare sovrapposizioni e mostro pulsante conferma e campi
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.listaScen.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("Orario attivazione (HH:MM)")
                self.campo3.setPlaceholderText("Orario disattivazione (HH:MM)")
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.show()
                self.click4 = 1
            #al secondo click, pulisco e nascondo i campi e nascondo anche il pulsante conferma
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click4 = 0

        #"associa_sens" si occupa di impostare il menù principale per l'aggiunta di sensori per l'automazione
        #è una funzione puramente grafica 
        def associa_sens(self):

            #al primo click:
            if self.click5 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = self.click1 = self.click2 = self.click4 = self.click3 = self.click6 = self.click7 = 0
                self.usoConferma = 4 #imposto usoConferma a 2 per modificare il funzionamento dl pulsante "conferma"
                #preparo il menù: pulisco i campi che mi servono e ne modifico il nome, nascondo la lista
                #per evitare sovrapposizioni e mostro pulsante conferma e campi
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.listaScen.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("ID Sensore da associare")
                self.campo3.setPlaceholderText("Valore soglia sensore")
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.show()
                self.click5 = 1
            #al secondo click, pulisco e nascondo i campi e nascondo anche il pulsante conferma
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click5 = 0

        #"diss_associa_att" si occupa di impostare il menù principale per l'aggiunta o la rimozione di attuatori per l'automazione
        #è una funzione puramente grafica 
        def diss_associa_att(self):
            
            #al primo click:
            if self.click6 == 0:
                #azzero gli altri contatori click per evitare di far sovrapporre i componenti gui
                self.click0 = self.click1 = self.click2 = self.click4 = self.click3 = self.click5 = self.click7 = 0
                self.usoConferma = 5 #imposto usoConferma a 2 per modificare il funzionamento dl pulsante "conferma"
                #preparo il menù: pulisco i campi che mi servono e ne modifico il nome, nascondo la lista
                #per evitare sovrapposizioni e mostro pulsante conferma e campi
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScen.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("ID Attuatore da +/-")
                [campo.show() for campo in [self.campo1, self.campo2]]
                self.btnConferma.show()
                self.click6 = 1
            #al secondo click, pulisco e nascondo i campi e nascondo anche il pulsante conferma
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click6 = 0

        #"indietro" riporta l'utente al menù principale della gui
        def indietro(self):
        
            from GUI.GUI_mainMenu import domOS_mainmenu
            self.finestra_mainmenu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_scenari, self.boundary_scenari, self.notifiche)
            self.finestra_mainmenu.show()
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
            campol = (larghezza * 20) // 100
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
            pulsantey1Menu = int(((altezza * 20) // 100) + 1.5*pulsanteaMenu)
            pulsantey2Menu = int(((altezza * 20) // 100) + 2.8*pulsanteaMenu)
            pulsantey3Menu = int(((altezza * 20) // 100) + 4.1*pulsanteaMenu)
            pulsantey4Menu = int(((altezza * 20) // 100) + 5.4*pulsanteaMenu)
            pulsantey5Menu = int(((altezza * 20) // 100) + 6.7*pulsanteaMenu)
            pulsantey6Menu = int(((altezza * 20) // 100) + 8*pulsanteaMenu)
            pulsantey7Menu = int(((altezza * 20) // 100) + 9.3*pulsanteaMenu)
            pulsantey8Menu = int(((altezza * 20) // 100) + 10.6*pulsanteaMenu)
            pulsantey9Menu = int(((altezza * 20) // 100) + 11.9*pulsanteaMenu)

            centroNx = int((larghezza * 7.5) // 100)
            centroNy = int((altezza * 1.5) // 100)
            centroNl = int((larghezza * 84) // 100)
            centroNa = int((altezza * 10) // 100)
            
            self.centroNotifiche.setGeometry(centroNx, centroNy, centroNl, centroNa)

            listaGenPurpx = int((larghezza * 40.5) // 100)
            listaGenPurpy = int((altezza * 14.7) // 100)
            listaGenPurpl = int((larghezza * 50) // 100)
            listaGenPurpa = int((altezza * 50) // 100)

            self.campo1.setGeometry(campox, campoy1, campol, campoa)
            self.campo2.setGeometry(campox, campoy2, campol, campoa)
            self.campo3.setGeometry(campox, campoy3, campol, campoa)

            self.btnConferma.setGeometry(pulsantexLog, pulsantey1Log, pulsantelLog, pulsanteaLog)

            self.btnLista.setGeometry(pulsantexMenu, pulsantey1Menu, pulsantelMenu, pulsanteaMenu)
            self.btnAdd.setGeometry(pulsantexMenu, pulsantey2Menu, pulsantelMenu, pulsanteaMenu)
            self.btnRemove.setGeometry(pulsantexMenu, pulsantey3Menu, pulsantelMenu, pulsanteaMenu)
            self.btnEdit.setGeometry(pulsantexMenu, pulsantey4Menu, pulsantelMenu, pulsanteaMenu)
            self.btnOra.setGeometry(pulsantexMenu, pulsantey5Menu, pulsantelMenu, pulsanteaMenu)
            self.btnAuto.setGeometry(pulsantexMenu, pulsantey6Menu, pulsantelMenu, pulsanteaMenu)
            self.btnAssocia.setGeometry(pulsantexMenu, pulsantey7Menu, pulsantelMenu, pulsanteaMenu)
            self.btnIndietro.setGeometry(pulsantexMenu, pulsantey9Menu, pulsantelMenu, pulsanteaMenu)

            self.listaScen.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)