class BoundaryDispositivo():
    def __init__(self, g_dati, g_disp):
        self._g_dati = g_dati 
        self._g_disp = g_disp


    
    def menu_disp(self, comando, id, tipo, nome, sogliaIn=None, stato_iniziale=None, orario_attivazione=None):
            
            if comando == "lista":
                self._g_disp.lista()
                
            elif comando == "aggiungi": # aggiungo dispositivo, chiedo i dati necessari e faccio il backup dopo ogni modifica
                
                if tipo == "sensore":
                    # Chiamata per il sensore passando il parametro soglia
                    feedback = self._g_disp.aggiungiDispositivo(id_disp=id, tipo=tipo, nome=nome, soglia=sogliaIn)
                    print(feedback)
                    
                elif tipo == "attuatore":
                    # Chiamata per l'attuatore passando i parametri kwargs stato e orario 
                    feedback = self._g_disp.aggiungiDispositivo(id_disp=id, tipo=tipo, nome=nome, stato=stato_iniziale, orario=orario_attivazione)
                    print(feedback)

                else:
                    print("Errore: Tipo dispositivo non valido. Operazione annullata.")
                dati = self._g_disp.tutte_to_dict()
                self._g_dati.esegui_backup(str(dati))
                

            elif comando == "rimuovi":
                
                feedback = self._g_disp.rimuoviDispositivo(id)
                print(feedback)
                #esegui backup dopo ogni modifica
                dati = self._g_disp.tutte_to_dict()
                self._g_dati.esegui_backup(dati)
                return feedback
                
            elif comando == "configura":
                #RICHIAMO DIRETTO DELLA FUNZIONE DAL G_DISP
                feedback = self._g_disp.configuraDispositivo(id, sogliaIn, stato_iniziale, orario_attivazione)
                print(feedback)

                #Salvataggio e backup
                dati = self._g_disp.tutte_to_dict()
                self._g_dati.esegui_backup(str(dati))

            else:
                print(f"Comando '{comando}' non riconosciuto.")

    def mostraStato(self):
        return self._g_dati.recupera_contenuto_backup()