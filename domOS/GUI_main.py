from Boundary.boundary_dispositivi_GUI import BoundaryDispositivo
from Boundary.boundary_utenti_GUI import BoundaryUtente
from Boundary.boundary_zone_GUI import BoundaryZona
from Boundary.boundary_scenari_GUI import BoundaryScenario
from Repos.dispositivo_repository import DispositivoRepository
from Repos.backup_repository import BackupRepository
from Repos.utente_repository import UtenteRepository
from Repos.zona_repository import ZonaRepository
from Repos.log_repository import LogRepository
from Repos.scenario_repository import ScenarioRepository
from Services.gestore_dati_GUI import GestoreDati
from Services.gestore_dispositivi_GUI import GestoreDispositivi
from Services.gestore_utenti_GUI import GestoreUtenti
from Services.gestore_zone_GUI import GestoreZona
from Services.gestore_scenari_GUI import GestoreScenario
from GUI.GUI_login import domOS_login
from Views.Timer import Timer
import json
import sys
from PyQt6.QtWidgets import (QApplication)

def main():
    print("Avvio")
    
    # Inizializzazione
    backup_repo = BackupRepository()
    dispositivo_repo = DispositivoRepository()
    utenti_repo = UtenteRepository()
    zona_repo = ZonaRepository()
    scenario_repo = ScenarioRepository()
    log_repo = LogRepository()

    g_dati = GestoreDati(backup_repo, log_repo)
    g_disp = GestoreDispositivi(dispositivo_repo)
    g_utenti = GestoreUtenti(utenti_repo)
    g_scenario = GestoreScenario(scenario_repo, g_disp, log_repo)
    g_zona = GestoreZona(zona_repo, g_disp, log_repo) #in questo caso passiamo anche g_disp per fare un check sull'esistenza di dispositivi prima di associarli

    boundary_disp = BoundaryDispositivo(g_dati, g_disp)
    boundary_utenti = BoundaryUtente(g_utenti, g_dati, utenti_repo)
    boundary_zone = BoundaryZona(g_zona)
    boundary_scenari = BoundaryScenario(g_scenario)

    # Ripristino dati
    dati_salvati = g_dati.recupera_contenuto_backup()
    if dati_salvati:
        print(f"[Ripristino] Stato ripristinato tramite backup: '{dati_salvati}'")
    else:
        print("[Ripristino] Nessun backup trovato. Avvio standard.")

    # Spazio definizione funzioni da eseguire periodicamente, e che prendano argomenti, come dati per backup o repo per check attuatori
    #se non definissimo queste funzioni ausiliarie, non potremmo passare argomenti ai metodi da eseguire periodicamente
    def backup(): 
        dati = dispositivo_repo.tutte()
        dati_convertiti = [d.toDict() for d in dati] #list comprehension trasforma i btnDisp in dizionari
        #in questo caso usiamo dumps invece di dump perché convertiamo in stringa, infatti esegui backup prende proprio una stringa come argomento
        stringa_dispositivi_backup = json.dumps(dati_convertiti, indent=4) #convertiamo in json così da poterli caricare nel file backup, l'indent me lo rende facilmente leggibile
        g_dati.esegui_backup(stringa_dispositivi_backup)   #li carichiamo nel file backup

    def esegui_check_attuatori():
        g_disp.check_attuatori(zona_repo)

    def esegui_automazioni_prioritarie():
        g_scenario.check_automazioni_prioritarie(g_zona)

    # Avvio timer
    timer_backup = Timer(azione_da_eseguire=backup, intervallo_secondi=360) #qui posso senza problemi passare backup, perché è una funzione che non richiede argomenti
    timer_backup.avvia()
    print("Controllo backup avviato con successo.")

    timer_attuatori = Timer(azione_da_eseguire=esegui_check_attuatori, intervallo_secondi=60) #qui posso passare la funzione perché "impacchetta"
    #la vera funzione di chec_attuatori, la quale di per se richiede argomenti
    timer_attuatori.avvia()

    timer_sensori = Timer(azione_da_eseguire = g_disp.check_sensori, intervallo_secondi=60)
    timer_sensori.avvia()

    timer_automazioni = Timer(azione_da_eseguire = esegui_automazioni_prioritarie, intervallo_secondi=60)
    timer_automazioni.avvia()

    #registrazione o autenticazione utente

    app = QApplication(sys.argv)
    f = domOS_login(boundary_disp, boundary_utenti, boundary_zone, boundary_scenari)
    f.show()

    sys.exit(app.exec())
if __name__ == "__main__":
    main()