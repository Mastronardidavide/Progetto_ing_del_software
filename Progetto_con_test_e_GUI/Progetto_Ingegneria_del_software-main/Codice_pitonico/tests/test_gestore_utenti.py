import unittest
import os
from Models.utente import Utente
from Repos.utente_repository import UtenteRepository
from Codice_pitonico.Services.gestore_utenti_GUI import GestoreUtenti

class TestGestoreUtenti(unittest.TestCase):

    def setUp(self):
        self.file_utenti = "test_utenti.json"
        self.utente_repo = UtenteRepository(self.file_utenti)
        self.utente_repo._utenti = {} 
        self.gestore = GestoreUtenti(self.utente_repo)
        
        # 1. Creiamo l'utente base passando 4 parametri, visto che il tipo è sempre "ospite"
        self.utente_base = Utente("U99", "UtenteTest", "password123", "ospite")
        self.utente_repo.aggiungi(self.utente_base)

    def test_crea_account_successo(self):
        # 2. Il metodo creaAccount invece riceve solo i 3 parametri richiesti
        risultato = self.gestore.creaAccount("U01", "Davide", "pass01")
        self.assertIn("creato", risultato.lower())
        
        utente_salvato = self.utente_repo.trovaPerId("U01")
        self.assertIsNotNone(utente_salvato)
        self.assertEqual(utente_salvato.getNome(), "Davide")
        self.assertEqual(len(self.utente_repo.tutti()), 2)

    def test_crea_account_duplicato(self):
        # 3 parametri
        risultato = self.gestore.creaAccount("U99", "NuovoNome", "pass02")
        self.assertIn("utente già presente", risultato.lower())
        
        utente_salvato = self.utente_repo.trovaPerId("U99")
        self.assertEqual(utente_salvato.getNome(), "UtenteTest")

    def test_elimina_account_successo(self):
        risultato = self.gestore.eliminaAccount("U99")
        self.assertIn("eliminato", risultato.lower())
        
        self.assertIsNone(self.utente_repo.trovaPerId("U99"))
        self.assertEqual(len(self.utente_repo.tutti()), 0)

    def test_elimina_account_non_esistente(self):
        risultato = self.gestore.eliminaAccount("U00")
        self.assertIn("non esiste", risultato.lower())

    def tearDown(self):
        if os.path.exists(self.file_utenti):
            os.remove(self.file_utenti)

if __name__ == '__main__':
    unittest.main()