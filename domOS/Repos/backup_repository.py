from datetime import datetime
import json
from pathlib import Path

#in questo modo l'implementazione è più snella rispetto ad avere una classe a parte che effettivamente si dovrebbe occupare esclusivamente di un solo dizionario
class BackupRepository:
    def __init__(self, path: str = "Data/backups.json"):
        self._path = self._risolvi_path(path)
        self._backup_corrente: dict = {} # Un singolo dizionario (backup) da sovrascrivere periodicamente
        self.carica()

    def _risolvi_path(self, path: str) -> Path:
        percorso = Path(path)
        if not percorso.is_absolute():
            percorso = Path(__file__).resolve().parent.parent / percorso
        return percorso

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                # Carica direttamente il singolo dizionario del backup
                self._backup_corrente = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._backup_corrente = {} # Se il file non esiste, il backup parte vuoto

    def salva(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._path, "w", encoding="utf-8") as f:
            # Salva il dizionario, ossia il backup
            json.dump(self._backup_corrente, f, indent=2, ensure_ascii=False)

    def sovrascrivi(self, contenuto_da_salvare: list | dict) -> None:
        # sovrascrive il vecchio backup
        self._backup_corrente = {
            "orario": datetime.now().isoformat(),
            "contenuto": json.dumps(contenuto_da_salvare, ensure_ascii=False)
        }
        self.salva()

    def getBackup(self) -> dict:
        # Ritorna l'unico backup presente in memoria
        return self._backup_corrente
    
