import unittest
from datetime import time # Il tuo codice usa 'time', importiamo quello corretto!

from Models.sensore import Sensore
from Models.attuatore import Attuatore

class TestSensore(unittest.TestCase):

    def setUp(self):
        self.sensore = Sensore("S01", "Termometro", "Sensore Salotto", 20.5)

    def test_stato_iniziale(self):
        self.assertEqual(self.sensore.getId(), "S01")
        self.assertEqual(self.sensore.getTipo(), "Termometro")
        self.assertEqual(self.sensore.getSoglia(), 20.5)
        self.assertEqual(self.sensore._nome, "Sensore Salotto")

    def test_set_soglia_successo(self):
        self.sensore.setSoglia(25.0)
        self.assertEqual(self.sensore.getSoglia(), 25.0)

    def test_set_soglia_errore(self):
        with self.assertRaises(TypeError):
            self.sensore.setSoglia("venticinque")

    def test_serializzazione(self):
        dizionario = self.sensore.toDict()
        
        nuovo_sensore = Sensore.fromDict(dizionario)
        self.assertEqual(nuovo_sensore.getId(), "S01")
        self.assertEqual(nuovo_sensore.getTipo(), "Termometro")
        self.assertEqual(nuovo_sensore.getSoglia(), 20.5)
        self.assertEqual(nuovo_sensore._nome, "Sensore Salotto")


class TestAttuatore(unittest.TestCase):
    
    def setUp(self):
        # Usiamo time() al posto di datetime()
        self.orario_test = time(14, 0)
        
        # Passiamo esattamente i 5 parametri del tuo costruttore:
        # id, tipo, nome, orarioAttivazione, statoAttuatore
        self.attuatore = Attuatore("A01", "Luce", "Luce Salotto", self.orario_test, False)

    def test_stato_iniziale(self):
        self.assertEqual(self.attuatore.getId(), "A01")
        self.assertEqual(self.attuatore.getTipo(), "Luce")
        self.assertEqual(self.attuatore._nome, "Luce Salotto")
        self.assertEqual(self.attuatore.getOrario(), self.orario_test)
        self.assertFalse(self.attuatore.getStato())

    def test_set_orario_successo(self):
        nuovo_orario = time(18, 30)
        self.attuatore.setOrario(nuovo_orario)
        self.assertEqual(self.attuatore.getOrario(), nuovo_orario)

    def test_cambia_stato(self):
        # Verifichiamo che il tuo metodo "toggle" funzioni correttamente
        self.attuatore.setStato(False)
        self.attuatore.cambiaStato()
        self.assertTrue(self.attuatore.getStato())

    def test_serializzazione(self):
        dizionario = self.attuatore.toDict()
        nuovo_attuatore = Attuatore.fromDict(dizionario)
        
        self.assertEqual(nuovo_attuatore.getId(), "A01")
        self.assertEqual(nuovo_attuatore.getTipo(), "Luce")
        self.assertEqual(nuovo_attuatore._nome, "Luce Salotto")
        self.assertEqual(nuovo_attuatore.getOrario(), self.orario_test)
        self.assertFalse(nuovo_attuatore.getStato())

if __name__ == '__main__':
    unittest.main()