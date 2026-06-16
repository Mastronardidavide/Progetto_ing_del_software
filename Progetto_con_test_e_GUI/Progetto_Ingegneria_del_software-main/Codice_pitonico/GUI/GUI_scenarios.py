from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QListWidget, QTextEdit, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

class domOS_scenarios(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari

            self.setWindowTitle("domOS")
            self.resize(800, 600)
            self.setMinimumSize(600, 400)

            self.listaScenari = QListWidget(self)
            self.listaScenari.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaScenari.hide()
            self.click0 = 0

            self.sfondo = QLabel(self)
            cartella_corrente = Path(__file__).resolve().parent
            percorso_immagine = cartella_corrente / "schermatamultipurpose_prot.png"
            percorso_str = str(percorso_immagine)
            self.pixmap_per_sfondo = QPixmap(percorso_str)

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

        def conferma(self):

            if self.usoConferma == 0:

                id_scen = self.campo1.text().strip()
                nome_scen = self.campo2.text().strip()
                comando = "aggiungi"
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
                
                self.boundary_scenari.menu_scenari(comando, id_scen, nome_scen)

                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Scenario aggiunto con successo!"
                )
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click1 = 0

            elif self.usoConferma == 1:

                id_scen = self.campo1.text().strip()
                comando = "rimuovi"
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
                    
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen)

                if feedback == f"Scenario eliminato":
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
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
            
            elif self.usoConferma == 2:

                id_edit = self.campo1.text().strip()
                nome_edit = self.campo2.text().strip()
                comando = "rinomina"

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
                
                self.boundary_scenari.menu_scenari(comando, id_edit, nome_edit)

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

            elif self.usoConferma == 3:

                id_scen = self.campo1.text().strip()
                orario1 = self.campo2.text().strip()
                orario2 = self.campo3.text().strip()
                comando = "orario"

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
                    
                nome = None
                self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off)
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

            elif self.usoConferma == 4:

                id_scen = self.campo1.text().strip()
                id_sens = self.campo2.text().strip()
                soglia = self.campo3.text().strip()
                comando = "automazione"

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
                
                check_soglia = False
                if not check_soglia:
                    try:
                        soglia_sens = float(soglia)
                        check_soglia = True

                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "Formato soglia non valido"
                        )
                        return
                    
                nome = orario_on = orario_off = None
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off, id_sens, soglia_sens)
                if feedback == f"Scenario non trovato":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Scenario non trovato")
                    return
                elif feedback == f"Errore: Il sensore con ID '{id_sens}' non esiste nella domotica. Automazione annullata.":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Sensore non trovato")
                    return
                elif feedback == f"Errore: Sensore e Soglia devono essere inseriti insieme.":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(
                        self, 
                        "Attenzione", 
                        "ID Sensore e Soglia devono essere inseriti insieme."
                        )
                    return
                
                else:
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

            elif self.usoConferma == 5:
                
                id_scen = self.campo1.text().strip()
                id_att = self.campo2.text().strip()
                comando = "associa"

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
                    
                nome = orario_on = orario_off = id_sens = soglia_sens = None
                feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off, id_sens, soglia_sens, id_att)
                if feedback == f"L'attuatore '{id_att}' è già associato a questa scenario":
                    if self.click7 == 0:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'Attuatore è già associato allo scenario. Premere 'Conferma' per dissociarlo o modificare il campo ID."
                            )
                        self.click7 += 1
                        return
                    
                    if self.click7 == 1:
                        comando = "dissocia"
                        feedback = self.boundary_scenari.menu_scenari(comando, id_scen, nome, orario_on, orario_off, id_sens, soglia_sens, id_att)
                        if feedback == f"Scenario non trovato":
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.critical(self, "Errore", "Scenario non trovato")
                            return
                        elif feedback == f"Errore: L'attuatore con ID '{id_att}' non esiste nel sistema.":
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.critical(self, "Errore", "Attuatore non trovato")
                            return
                        elif feedback == f"Attuatore '{id_att}' rimosso dallo scenario con successo":
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

        def lista(self):

            if self.click0 == 0:
                self.click1 = self.click4 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.listaScenari.clear()
                self.listaScenari.addItem("Lista Scenari presenti nel sistema")
                self.listaScenari.addItem("_" * 40)
                lista_scen = self.boundary_scenari.menu_scenari("lista")
                if not lista_scen:
                    self.listaScenari.addItem("Nessuno Scenario registrato nel sistema.")
                for scenario_oggetto in lista_scen:
                    scenario = scenario_oggetto.toDict()
                    id_scen = scenario.get("id", "N/D")
                    nome_scen = scenario.get("nome", "Sconosciuto")
                    orarioattivazione = scenario.get("orarioScenario", "N/D")
                    orariodisattivazione = scenario.get("orarioDisattivazione", "N/D")
                    sogliascen = scenario.get("sogliaScenario", "N/D")
                    id_sens = scenario.get("id_sensore", "N/D")
                    id_att = scenario.get("id_attuatori", [])
                    if not id_att:
                        attuatori_str = "None"
                    else:
                        attuatori_str = ", ".join(id_att)
                    riga_testo = (f"[ID: {id_scen}] - Scenario: {nome_scen}\n"
                                  f"Attivazione: {orarioattivazione} - Disattivazione: {orariodisattivazione} - Soglia: {sogliascen}\n"
                                  f"Sensore [ID]: {id_sens} - Attuatori [ID]: {attuatori_str}"  
                    )
                    self.listaScenari.addItem(riga_testo)
                    self.listaScenari.addItem("_" * 40)
                self.listaScenari.show()
                self.listaScenari.raise_()
                self.click0 += 1

            else:
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.listaScenari.clear()
                self.listaScenari.hide()
                self.click0 += 1
            if self.click0 >=2:
                 self.click0 = 0
                 
        def aggiungi(self):

            if self.click1 == 0:
                self.click0 = self.click4 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 0
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScenari.hide()
                self.campo1.setPlaceholderText("ID Nuovo Scenario")
                self.campo2.setPlaceholderText("Nome Nuovo Scenario")
                [campo.show() for campo in [self.campo1, self.campo2]]
                self.btnConferma.show()
                self.click1 += 1
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click1 += 1

            if self.click1 >= 2:
                self.click1 = 0

        def rimuovi(self):
            
            if self.click2 == 0:
                self.click0 = self.click1 = self.click4 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 1
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScenari.hide()
                self.campo1.setPlaceholderText("ID Scenario da eliminare")
                self.campo1.show()
                self.btnConferma.show()
                self.click2 += 1
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click2 += 1

            if self.click2 >= 2:
                self.click2 = 0

        def rinomina(self):

            if self.click3 == 0:
                self.click0 = self.click1 = self.click2 = self.click4 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 2
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScenari.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("Nuovo nome")
                [campo.show() for campo in [self.campo1, self.campo2]]
                self.btnConferma.show()
                self.click3 += 1
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click3 += 1

            if self.click3 >= 2:
                self.click3 = 0

        def orario(self):

            if self.click4 == 0:
                self.click0 = self.click1 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 3
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.listaScenari.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("Orario attivazione (HH:MM)")
                self.campo3.setPlaceholderText("Orario disattivazione (HH:MM)")
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.show()
                self.click4 += 1
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click4 += 1

            if self.click4 >= 2:
                self.click4 = 0

        def associa_sens(self):

            if self.click5 == 0:
                self.click0 = self.click1 = self.click2 = self.click4 = self.click3 = self.click6 = self.click7 = 0
                self.usoConferma = 4
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.listaScenari.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("ID Sensore da associare")
                self.campo3.setPlaceholderText("Valore soglia sensore")
                [campo.show() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.show()
                self.click5 += 1
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click5 += 1

            if self.click5 >= 2:
                self.click5 = 0

        def diss_associa_att(self):
            
            if self.click6 == 0:
                self.click0 = self.click1 = self.click2 = self.click4 = self.click3 = self.click5 = self.click7 = 0
                self.usoConferma = 5
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaScenari.hide()
                self.campo1.setPlaceholderText("ID Scenario")
                self.campo2.setPlaceholderText("ID Attuatore da +/-")
                [campo.show() for campo in [self.campo1, self.campo2]]
                self.btnConferma.show()
                self.click6 += 1
            else:
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click6 += 1

            if self.click6 >= 2:
                self.click6 = 0

        def indietro(self):

            from GUI.GUI_mainMenu import domOS_mainmenu
            self.finestra_mainmenu = domOS_mainmenu(self.boundary_disp, self.boundary_utenti, self.boundary_scenari, self.boundary_scenari)
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

            self.listaScenari.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)