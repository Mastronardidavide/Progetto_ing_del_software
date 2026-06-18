import unittest
from datetime import time

# Assicurati che l'import punti al file corretto nel tuo package Models
from Models.zona import Zona

class TestZona(unittest.TestCase):

    def setUp(self):
        # 1. Arrange: Prepariamo due orari e una Zona completa per ogni test
        self.orario_att = time(8, 0)
        self.orario_dis = time(20, 30)
        
        self.zona = Zona(
            id=10, 
            nome="Zona Giorno", 
            orarioZona=self.orario_att, 
            sogliaZona=21.5, 
            id_attuatori=["A01", "A02"], 
            id_sensore="S01", 
            orarioDisattivazione=self.orario_dis
        )

    def test_stato_iniziale(self):
        # Verifica che il costruttore salvi tutto correttamente (Assert)
        self.assertEqual(self.zona.getId(), 10)
        self.assertEqual(self.zona.getNome(), "Zona Giorno")
        self.assertEqual(self.zona.getOrarioZona(), self.orario_att)
        self.assertEqual(self.zona.getSogliaZona(), 21.5)
        self.assertEqual(self.zona.getIdAttuatori(), ["A01", "A02"])
        self.assertEqual(self.zona.getIdSensore(), "S01")
        self.assertEqual(self.zona.getOrarioDisattivazione(), self.orario_dis)

    def test_imposta_soglia_successo(self):
        # Verifica la logica del setter
        self.zona.impostaSoglia(24.0)
        self.assertEqual(self.zona.getSogliaZona(), 24.0)

    def test_imposta_soglia_errore(self):
        # Verifica la Gestione Errori: la tua eccezione scatta se passo una stringa
        with self.assertRaises(TypeError):
            self.zona.impostaSoglia("ventiquattro")

    def test_associa_e_rimuovi_attuatore(self):
        # Verifica che i metodi per gestire la lista degli attuatori funzionino
        self.zona.associaAttuatore("A03")
        self.assertIn("A03", self.zona.getIdAttuatori())
        
        self.zona.rimuoviAttuatore("A01")
        self.assertNotIn("A01", self.zona.getIdAttuatori())
        # A02 e A03 dovrebbero ancora esserci
        self.assertEqual(len(self.zona.getIdAttuatori()), 2)

    def test_serializzazione(self):
        # Verifica che toDict e fromDict convertano correttamente i dati (inclusi i "time")
        dizionario = self.zona.toDict()
        
        nuova_zona = Zona.fromDict(dizionario)
        
        self.assertEqual(nuova_zona.getId(), 10)
        self.assertEqual(nuova_zona.getNome(), "Zona Giorno")
        self.assertEqual(nuova_zona.getOrarioZona(), self.orario_att)
        self.assertEqual(nuova_zona.getSogliaZona(), 21.5)
        self.assertEqual(nuova_zona.getIdAttuatori(), ["A01", "A02"])
        self.assertEqual(nuova_zona.getIdSensore(), "S01")
        self.assertEqual(nuova_zona.getOrarioDisattivazione(), self.orario_dis)

    def test_serializzazione_valori_none(self):
        # Verifica cruciale: assicuriamoci che se la Zona ha campi vuoti (None),
        # la deserializzazione di time.fromisoformat non faccia crashare il sistema.
        zona_vuota = Zona(id=11)
        diz_vuoto = zona_vuota.toDict()
        
        nuova_zona_vuota = Zona.fromDict(diz_vuoto)
        self.assertEqual(nuova_zona_vuota.getId(), 11)
        self.assertIsNone(nuova_zona_vuota.getOrarioZona())
        self.assertEqual(nuova_zona_vuota.getIdAttuatori(), [])

if __name__ == '__main__':
    unittest.main()