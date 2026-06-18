from PyQt6.QtCore import QObject, pyqtSignal #import di librerie per lo scambio di messaggi nel codice
class BoundaryDispositivo(QObject):

    #parte cruciale: datochè il timer lavora in un thread diverso dalla GUI, è impossibile
    #farli comunicare direttamente per permettere lo scambio di notifiche (ad esempio tramite return).
    #Per questo motivo si utilizza pyqtSignal, che permette la creazione di 
    #veri e propri canali di informazione attraverso i quali è possibile
    #far comunicare pvari componenti del codice tra loro

    notificaAtt = pyqtSignal(str)   #genero i canali di trasmissione
    notificaSens = pyqtSignal(str)
    notificaAuto = pyqtSignal(str)

    def __init__(self, g_dati, g_disp, g_zona, g_scenario):
        super().__init__()
        self._g_dati = g_dati 
        self._g_disp = g_disp
        self._g_zona = g_zona
        self._g_scenario = g_scenario

    
    def menu_disp(self, comando, id, tipo, nome, sogliaIn=None, stato_iniziale=None, orario_attivazione=None):
            
            if comando == "lista":
                self._g_disp.lista()
                
            elif comando == "aggiungi": # aggiungo dispositivo, chiedo i dati necessari e faccio il backup dopo ogni modifica
                
                if tipo == "sensore":
                    # Chiamata per il sensore passando il parametro soglia
                    feedback = self._g_disp.aggiungiDispositivo(id_disp=id, tipo=tipo, nome=nome, soglia=sogliaIn)
                    return feedback
                    
                elif tipo == "attuatore":
                    # Chiamata per l'attuatore passando i parametri kwargs stato e orario 
                    feedback = self._g_disp.aggiungiDispositivo(id_disp=id, tipo=tipo, nome=nome, stato=stato_iniziale, orario=orario_attivazione)
                    return feedback

                dati = self._g_disp.tutte_to_dict()
                self._g_dati.esegui_backup(str(dati))
                

            elif comando == "rimuovi":
                
                feedback = self._g_disp.rimuoviDispositivo(id)
                #esegui backup dopo ogni modifica
                dati = self._g_disp.tutte_to_dict()
                self._g_dati.esegui_backup(dati)
                return feedback
                
            elif comando == "configura":
                #RICHIAMO DIRETTO DELLA FUNZIONE DAL G_DISP
                feedback = self._g_disp.configuraDispositivo(id, sogliaIn, stato_iniziale, orario_attivazione)

                #Salvataggio e backup
                dati = self._g_disp.tutte_to_dict()
                self._g_dati.esegui_backup(str(dati))
                return feedback

    def mostraStato(self):
        return self._g_dati.recupera_contenuto_backup()
    
    def check(self, tipo):
        if tipo == "attuatore":
            repo_zone = self._g_zona.getRepo()
            feedback = self._g_disp.check_attuatori(repo_zone)
            if feedback is not None:
                self.notificaAtt.emit(feedback) #ogni volta che il timer esegue un check, invio il risultato sui canali.
        elif tipo == "sensore":
            feedback = self._g_disp.check_sensori()
            if feedback is not None:
                self.notificaSens.emit(feedback)
        elif tipo == "automazioni":
            feedback = self._g_scenario.check_automazioni_prioritarie(self._g_zona)
            if feedback is not None:
                self.notificaAuto.emit(feedback)
    def backup(self, data):
        self._g_dati.esegui_backup(data)