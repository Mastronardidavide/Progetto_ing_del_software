from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QListWidget, QTextEdit, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel

class domOS_zones(QWidget): 
        def __init__(self, boundary_disp, boundary_utenti, boundary_zone, boundary_scenari):
            super().__init__()
            
            self.boundary_disp = boundary_disp
            self.boundary_utenti = boundary_utenti
            self.boundary_zone = boundary_zone
            self.boundary_scenari = boundary_scenari

            self.setWindowTitle("domOS")
            self.resize(800, 600)
            self.setMinimumSize(600, 400)

            self.listaZone = QListWidget(self)
            self.listaZone.setStyleSheet("""
                background-color: #3a7bff;
                border: 2px solid #ccc;
                border-radius: 8px;
                color: white;
            """)
            self.listaZone.hide()
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

            self.btnLista = QPushButton("Lista Zone", self)
            self.btnLista.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnLista.clicked.connect(self.lista)
            self.click0 = 0

            self.btnAdd = QPushButton("Aggiungi Zona", self)
            self.btnAdd.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnAdd.clicked.connect(self.aggiungi)
            self.click1 = 0

            self.btnRemove = QPushButton("Rimuovi Zona", self)
            self.btnRemove.setStyleSheet("""
                background-color: #3a7bff;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            """)
            self.btnRemove.clicked.connect(self.rimuovi)
            self.click2 = 0

            self.btnEdit = QPushButton("Rinomina Zona", self)
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

                id_zona = self.campo1.text().strip()
                nome_zona = self.campo2.text().strip()
                comando = "aggiungi"
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(id_zona) 
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
                
                self.boundary_zone.menu_zone(comando, id_zona, nome_zona)
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Zona aggiunta con successo!"
                )
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click1 = 0

            elif self.usoConferma == 1:

                id_zona = self.campo1.text().strip()
                comando = "rimuovi"
                check_id = False
            
                if not check_id:
                    try:
                        id_valore = int(id_zona) 
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
                    
                feedback = self.boundary_zone.menu_zone(comando, id_zona)

                if feedback == f"Zona eliminata":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.information(
                        self, 
                        "Successo", 
                        "Zona eliminata con successo!"
                    )
                    [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                    [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                    self.btnConferma.hide()
                    self.click2 = 0

                elif feedback == f"Zona non trovata":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Zona non trovata")
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
                
                self.boundary_zone.menu_zone(comando, id_edit, nome_edit)
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Nome Zona modificato con successo!"
                )
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click3 = 0

            elif self.usoConferma == 3:

                id_zona = self.campo1.text().strip()
                orario1 = self.campo2.text().strip()
                orario2 = self.campo3.text().strip()
                comando = "orario"

                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_zona) 
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
                self.boundary_zone.menu_zone(comando, id_zona, nome, orario_on, orario_off)

                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.information(
                    self, 
                    "Successo", 
                    "Pianificazione zona completata!"
                )
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.click4 = 0

            elif self.usoConferma == 4:

                id_zona = self.campo1.text().strip()
                id_sens = self.campo2.text().strip()
                soglia = self.campo3.text().strip()
                comando = "automazione"

                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_zona) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID Zona deve essere un numero intero positivo."
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
                feedback = self.boundary_zone.menu_zone(comando, id_zona, nome, orario_on, orario_off, id_sens, soglia_sens)
                if feedback == f"Zona non trovata":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Zona non trovata")
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
                
                id_zona = self.campo1.text().strip()
                id_att = self.campo2.text().strip()
                comando = "associa"

                check_id = False
                if not check_id:
                    try:
                        id_valore = int(id_zona) 
                        if id_valore <= 0:
                            raise ValueError
                        check_id = True
                    except ValueError:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'ID Zona deve essere un numero intero positivo."
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
                feedback = self.boundary_zone.menu_zone(comando, id_zona, nome, orario_on, orario_off, id_sens, soglia_sens, id_att)
                if feedback == f"L'attuatore '{id_att}' è già associato a questa zona":
                    if self.click7 == 0:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(
                            self, 
                            "Attenzione", 
                            "L'Attuatore è già associato alla zona. Premere 'Conferma' per dissociarlo o modificare il campo ID."
                            )
                        self.click7 += 1
                        return
                    
                    if self.click7 == 1:
                        comando = "dissocia"
                        feedback = self.boundary_zone.menu_zone(comando, id_zona, nome, orario_on, orario_off, id_sens, soglia_sens, id_att)
                        if feedback == f"Zona non trovata":
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.critical(self, "Errore", "Zona non trovata")
                            return
                        elif feedback == f"Errore: L'attuatore con ID '{id_att}' non esiste nel sistema.":
                            from PyQt6.QtWidgets import QMessageBox
                            QMessageBox.critical(self, "Errore", "Attuatore non trovato")
                            return
                        elif feedback == f"Attuatore '{id_att}' rimosso dalla zona con successo":
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

                elif feedback == f"Zona non trovata":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Zona non trovata")
                    return
                elif feedback == f"Errore: L'attuatore con ID '{id_att}' non esiste nel sistema.":
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.critical(self, "Errore", "Attuatore non trovato")
                    return
                elif feedback == f"Attuatore '{id_att}' associato alla zona con successo":
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
                self.listaZone.clear()
                self.listaZone.addItem("Lista Zone presenti nel sistema")
                self.listaZone.addItem("_" * 40)
                lista_zone = self.boundary_zone.menu_zone("lista")
                if not lista_zone:
                    self.listaZone.addItem("Nessuna zona registrata nel sistema.")
                for zona in lista_zone:
                    id_zona = zona.get("id", "N/D")
                    nome_zona = zona.get("nome", "Sconosciuto")
                    orarioattivazione = zona.get("orarioZona", "N/D")
                    orariodisattivazione = zona.get("orarioDisattivazione", "N/D")
                    sogliazona = zona.get("sogliaZona", "N/D")
                    id_sens = zona.get("id_sensore", "N/D")
                    id_att = zona.get("id_attuatori", [])
                    if not id_att:
                        attuatori_str = "None"
                    else:
                        attuatori_str = ", ".join(id_att)
                    riga_testo = (f"[ID: {id_zona}] - Zona: {nome_zona}\n"
                                  f"Attivazione: {orarioattivazione} - Disattivazione: {orariodisattivazione} - Soglia: {sogliazona}\n"
                                  f"Sensore [ID]: {id_sens} - Attuatori [ID]: {attuatori_str}"  
                    )
                    self.listaZone.addItem(riga_testo)
                    self.listaZone.addItem("_" * 40)
                self.listaZone.show()
                self.listaZone.raise_()
                self.click0 += 1

            else:
                [campo.hide() for campo in [self.campo1, self.campo2, self.campo3]]
                self.btnConferma.hide()
                self.listaZone.clear()
                self.listaZone.hide()
                self.click0 += 1
            if self.click0 >=2:
                 self.click0 = 0
                 
        def aggiungi(self):

            if self.click1 == 0:
                self.click0 = self.click4 = self.click2 = self.click3 = self.click5 = self.click6 = self.click7 = 0
                self.usoConferma = 0
                [campo.clear() for campo in [self.campo1, self.campo2, self.campo3]]
                self.campo3.hide()
                self.listaZone.hide()
                self.campo1.setPlaceholderText("ID Nuova Zona")
                self.campo2.setPlaceholderText("Nome Nuova Zona")
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
                self.listaZone.hide()
                self.campo1.setPlaceholderText("ID Zona da eliminare")
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
                self.listaZone.hide()
                self.campo1.setPlaceholderText("ID Zona")
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
                self.listaZone.hide()
                self.campo1.setPlaceholderText("ID Zona")
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
                self.listaZone.hide()
                self.campo1.setPlaceholderText("ID Zona")
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
                self.listaZone.hide()
                self.campo1.setPlaceholderText("ID Zona")
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

            self.listaZone.setGeometry(listaGenPurpx, listaGenPurpy, listaGenPurpl, listaGenPurpa)
            super().resizeEvent(event)