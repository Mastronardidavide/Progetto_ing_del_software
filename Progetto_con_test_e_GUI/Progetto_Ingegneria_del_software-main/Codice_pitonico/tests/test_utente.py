import unittest
# Importiamo la classe Utente dal tuo package Models
from Models.utente import Utente

class TestUtente(unittest.TestCase): #la classe test utente eredita da unittest.TestCase
    #dice a python che non è una classe normale ma una "suite di test"
    
    def setUp(self):
        # Fase 1 - Arrange: viene eseguito prima di ogni test.
        # Permette di avere un oggetto "pulito" su cui fare le verifiche.
        self.utente = Utente("U01", "Davide", "password123", "Ospite")

    def test_stato_iniziale(self):
        # Fase 3 - Assert: Verifichiamo che il costruttore abbia 
        # assegnato correttamente l'ID e il nome.
        self.assertEqual(self.utente.getId(), "U01")
        self.assertEqual(self.utente.getNome(), "Davide")
        self.assertEqual(self.utente.getTipo(), "Ospite")

    def test_to_dict(self):
        # Fase 2 - Act: proviamo a convertire l'oggetto in dizionario
        dizionario = self.utente.toDict()
        
        # Fase 3 - Assert: controlliamo che le chiavi e i valori siano corretti
        self.assertEqual(dizionario["id"], "U01")
        self.assertEqual(dizionario["nome"], "Davide")
        self.assertEqual(dizionario["password"], "password123")
        self.assertEqual(dizionario["tipo"], "Ospite")

    def test_from_dict(self):
        # Fase 1 - Arrange: prepariamo un dizionario fittizio
        dati_salvati = {
            "id": "U02",
            "nome": "Federico",
            "password": "abc123",
            "tipo": "Admin"
        }
        
        # Fase 2 - Act: invochiamo il costruttore alternativo (classmethod)
        nuovo_utente = Utente.fromDict(dati_salvati)
        
        # Fase 3 - Assert: verifichiamo che l'oggetto ricreato sia corretto
        self.assertEqual(nuovo_utente.getId(), "U02")
        self.assertEqual(nuovo_utente.getNome(), "Federico")
        self.assertEqual(nuovo_utente.getTipo(), "Admin")

    def test_autentica(self):
        # Testiamo il login corretto (Davide)
        self.assertTrue(self.utente.autentica("Davide", "password123"))
        
        # Testiamo il login fallito per password errata
        self.assertFalse(self.utente.autentica("Davide", "password_sbagliata"))
        
        # Testiamo il login fallito per nome utente errato (Riccardo cerca di accedere al profilo di Davide!)
        self.assertFalse(self.utente.autentica("Riccardo", "password123"))

    def test_str_formattazione(self):
        # Verifichiamo che il dunder method __str__ produca l'output desiderato
        stringa_attesa = "Davide (id: U01, tipo: Ospite)"
        self.assertEqual(str(self.utente), stringa_attesa)

if __name__ == '__main__':
    unittest.main()