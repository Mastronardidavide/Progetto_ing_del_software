import unittest
from datetime import time

# Assicurati che l'import punti al file corretto nel tuo progetto
from Models.scenario import Scenario
from Models.attuatore import Attuatore
from Models.sensore import Sensore


class TestScenario(unittest.TestCase):

    def setUp(self):
        # 1. Arrange: Prepariamo due orari e uno scenario completo per ogni test
        self.orario_att = time(18, 0)
        self.orario_disatt = time(23, 30)
        
        self.scenario = Scenario(
            id=1, 
            nome="Scenario Serale", 
            orarioScenario=self.orario_att, 
            sogliaScenario=22.5, 
            id_attuatori=["A01", "A02"], 
            id_sensore="S01", 
            orarioDisattivazione=self.orario_disatt
        )

    def test_stato_iniziale(self):
        # Verifica che il costruttore salvi tutto correttamente
        self.assertEqual(self.scenario.getId(), 1)
        self.assertEqual(self.scenario.getNome(), "Scenario Serale")
        self.assertEqual(self.scenario.getOrarioScenario(), self.orario_att)
        self.assertEqual(self.scenario.getSogliaScenario(), 22.5)
        self.assertEqual(self.scenario.getIdAttuatori(), ["A01", "A02"])
        self.assertEqual(self.scenario.getIdSensore(), "S01")
        self.assertEqual(self.scenario.getOrarioDisattivazione(), self.orario_disatt)

    def test_imposta_soglia_successo(self):
        # Verifica la logica del setter
        self.scenario.impostaSoglia(25.0)
        self.assertEqual(self.scenario.getSogliaScenario(), 25.0)

    def test_imposta_soglia_errore(self):
        # Verifica la Gestione Errori: il tuo TypeError scatta se passo una stringa
        with self.assertRaises(TypeError):
            self.scenario.impostaSoglia("venticinque")

    def test_associa_e_rimuovi_attuatore(self):
        # Verifica i metodi specifici per le liste
        self.scenario.associaAttuatore("A03")
        self.assertIn("A03", self.scenario.getIdAttuatori())
        
        self.scenario.rimuoviAttuatore("A01")
        self.assertNotIn("A01", self.scenario.getIdAttuatori())
        # A02 e A03 dovrebbero ancora esserci
        self.assertEqual(len(self.scenario.getIdAttuatori()), 2)

    def test_serializzazione(self):
        # Verifica che toDict e fromDict convertano correttamente anche i "time"
        dizionario = self.scenario.toDict()
        
        nuovo_scenario = Scenario.fromDict(dizionario)
        
        self.assertEqual(nuovo_scenario.getId(), 1)
        self.assertEqual(nuovo_scenario.getNome(), "Scenario Serale")
        self.assertEqual(nuovo_scenario.getOrarioScenario(), self.orario_att)
        self.assertEqual(nuovo_scenario.getSogliaScenario(), 22.5)
        self.assertEqual(nuovo_scenario.getIdAttuatori(), ["A01", "A02"])
        self.assertEqual(nuovo_scenario.getIdSensore(), "S01")
        self.assertEqual(nuovo_scenario.getOrarioDisattivazione(), self.orario_disatt)

    def test_serializzazione_valori_none(self):
        # Verifica secondaria: se lo scenario è vuoto, i "time" a None non devono far crashare fromDict
        scenario_vuoto = Scenario(id=2)
        diz_vuoto = scenario_vuoto.toDict()
        
        nuovo_scenario_vuoto = Scenario.fromDict(diz_vuoto)
        self.assertEqual(nuovo_scenario_vuoto.getId(), 2)
        self.assertIsNone(nuovo_scenario_vuoto.getOrarioScenario())
        self.assertEqual(nuovo_scenario_vuoto.getIdAttuatori(), [])

if __name__ == '__main__':
    unittest.main()