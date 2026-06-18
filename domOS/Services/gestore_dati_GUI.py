from Repos.backup_repository import BackupRepository

class GestoreDati:
    def __init__(self, backup_repo: BackupRepository, log_repo):
        self._backup_repo = backup_repo
        self._log_repo = log_repo

    def esegui_backup(self, stringa_dati: str) -> None:

        try:
            self._backup_repo.sovrascrivi(stringa_dati)
        except Exception as e:
            self._log_repo.scriviErrore(f"GestoreDati: Salvataggio automatico fallito. Dettaglio: {str(e)}")
        return "scrivibackup"
    
    def recupera_contenuto_backup(self) -> str:
        return self._backup_repo.getBackup()
