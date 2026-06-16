from datetime import datetime

class BoundaryZona:
    def __init__(self, g_zona):
        """ Riceve l'istanza del GestoreZona per operare sulle zone """
        self._g_zona = g_zona

    def menu_zone(self, comando, id_zona=None, nome=None, orario_inizio=None, orario_fine=None, id_sensore=None, soglia=None, id_att=None):

            """print("\n=======================================================")
            print("Gestione Zone: \n'lista' (mostra zone) \n'aggiungi' (crea nuova zona) \n'rimuovi' (elimina zona)")
            print("'rinomina' (aggiorna nome) \n'orario' (imposta finestra temporale) \n'automazione' (imposta sensore+soglia)")
            print("'associa' (collega attuatore) \n'disassocia' (rimuovi attuatore) \n'indietro' (torna al menu principale)")
            print("=======================================================\n")"""
            
            if comando == "lista":
                return self._g_zona.tuttiToDict()
            elif comando == "aggiungi":
                feedback = self._g_zona.creaZona(id=id_zona, nome=nome)
                print(f"\n[Nuova zona]: {feedback}")
                
            elif comando == "rimuovi":
                feedback = self._g_zona.eliminaZona(id=id_zona)
                print(feedback)
                return feedback
            
            elif comando == "rinomina":
                feedback = self._g_zona.modificaZona(id=id_zona, nuovo_nome=nome)
                print(feedback)

            elif comando == "orario":
                # Chiamata alla funzione del gestore
                feedback = self._g_zona.impostaProgrammazioneOraria(id_zona=id_zona, orario_inizio=orario_inizio, orario_fine=orario_fine)
                print(feedback)

            elif comando == "automazione":
                
                feedback = self._g_zona.impostaAutomazioneSensore(id_zona=id_zona, id_sensore=id_sensore, valore_soglia=soglia)
                print(feedback)

            elif comando == "associa":
                
                feedback = self._g_zona.associaAttuatoreAZona(id_zona=id_zona, id_attuatore=id_att)
                print(feedback)
                return feedback
            elif comando == "dissocia":
                
                feedback = self._g_zona.rimuoviAttuatoreDaZona(id_zona=id_zona, id_attuatore=id_att)
                print(feedback)
                return feedback
