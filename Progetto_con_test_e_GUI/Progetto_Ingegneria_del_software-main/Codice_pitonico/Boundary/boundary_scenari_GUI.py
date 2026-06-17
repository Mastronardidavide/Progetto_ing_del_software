class BoundaryScenario:
    def __init__(self, g_scenario):
        self._g_scenario = g_scenario

    def menu_scenari(self, comando, id_scenario=None, nome=None, orario_inizio=None, orario_fine=None, id_sensore=None, soglia=None, id_att=None):
   
            if comando == "lista":
                scenari = self._g_scenario._scenario_repo.tutte()
                return scenari
            
            elif comando == "aggiungi":
                feedback = self._g_scenario.creaScenario(id=id_scenario, nome=nome)
                print(f"\n[Nuovo scenario]: {feedback}")
                return feedback
            
            elif comando == "rimuovi":
                feedback = self._g_scenario.eliminaScenario(id=id_scenario)
                print(feedback)
                return feedback

            elif comando == "rinomina":
                feedback = self._g_scenario.modificaScenario(id=id_scenario, nuovo_nome=nome)
                print(feedback)
                return feedback

            elif comando == "orario":
                feedback = self._g_scenario.impostaProgrammazioneOraria(id_scenario=id_scenario, orario_inizio=orario_inizio, orario_fine=orario_fine)
                print(feedback)
                return feedback
            
            elif comando == "automazione":
                feedback = self._g_scenario.impostaAutomazioneSensore(id_scenario=id_scenario, id_sensore=id_sensore, valore_soglia=soglia)
                print(feedback)
                return feedback

            elif comando == "associa":
                feedback = self._g_scenario.associaAttuatoreAScenario(id_scenario=id_scenario, id_attuatore=id_att)
                print(feedback)
                return feedback

            elif comando == "dissocia":
                feedback = self._g_scenario.rimuoviAttuatoreDaScenario(id_scenario=id_scenario, id_attuatore=id_att)
                print(feedback)
                return feedback

