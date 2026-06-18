class BoundaryZona:
    def __init__(self, g_zona):
        """ Riceve l'istanza del GestoreZona per operare sulle zone """
        self._g_zona = g_zona

    def menu_zone(self, comando, id_zona=None, nome=None, orario_inizio=None, orario_fine=None, id_sensore=None, soglia=None, id_att=None):

            if comando == "lista":
                return self._g_zona.tuttiToDict()
            elif comando == "aggiungi":
                feedback = self._g_zona.creaZona(id=id_zona, nome=nome)
                return feedback
            
            elif comando == "rimuovi":
                feedback = self._g_zona.eliminaZona(id=id_zona)
                return feedback
            
            elif comando == "rinomina":
                feedback = self._g_zona.modificaZona(id=id_zona, nuovo_nome=nome)
                return feedback

            elif comando == "orario":
                # Chiamata alla funzione del gestore
                feedback = self._g_zona.impostaProgrammazioneOraria(id_zona=id_zona, orario_inizio=orario_inizio, orario_fine=orario_fine)
                return feedback

            elif comando == "automazione":
                feedback = self._g_zona.impostaAutomazioneSensore(id_zona=id_zona, id_sensore=id_sensore, valore_soglia=soglia)
                return feedback

            elif comando == "associa":
                
                feedback = self._g_zona.associaAttuatoreAZona(id_zona=id_zona, id_attuatore=id_att)
                return feedback
            elif comando == "dissocia":
                
                feedback = self._g_zona.rimuoviAttuatoreDaZona(id_zona=id_zona, id_attuatore=id_att)
                return feedback
