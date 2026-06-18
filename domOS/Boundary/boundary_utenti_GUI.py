class BoundaryUtente:
    def __init__(self, g_utenti, g_dati, utenti_repo):
        self._g_utenti = g_utenti
        self._g_dati = g_dati
        self._utenti_repo = utenti_repo

    def form_registrazione(self, id_ut, nome, pswd):
       
        feedback = self._g_utenti.creaAccount(id=id_ut, nome=nome, pswd=pswd)
        return feedback

    def form_login(self, id_ut, nome, pswd):
        # Delega il controllo delle credenziali al Gestore Utenti
        utente = self._g_utenti.login(id=id_ut, nome=nome, pswd=pswd)
        return utente

    def menu_utente(self, comando, id_ut):
    
            if comando == "elimina":
                
                feedback = self._g_utenti.eliminaAccount(id=id_ut)
                # Esecuzione del backup dopo l'eliminazione
                dati = self._g_utenti.tuttiToDict()
                self._g_dati.esegui_backup(str(dati))
                return feedback

            elif comando == "lista":
                 return self._g_utenti.tuttiToDict()
