from Repos.backup_repository import BackupRepository

class GestoreDati:
    def __init__(self, backup_repo: BackupRepository, log_repo):
        self._backup_repo = backup_repo
        self._log_repo = log_repo

    def esegui_backup(self, lista_dati: list) -> None:
        try:
            self._backup_repo.sovrascrivi(lista_dati)
            return "ok"
        except Exception as e:
            self._log_repo.scriviErrore(f"GestoreDati: Salvataggio automatico fallito. Dettaglio: {str(e)}")
            return e
    def recupera_contenuto_backup(self) -> str:
        return self._backup_repo.getBackup()
