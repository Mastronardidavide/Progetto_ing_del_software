import json
from pathlib import Path
from Models.sensore import Sensore
from Models.attuatore import Attuatore

class DispositivoRepository:
    def __init__(self, path: str = "Data/dispositivi.json"):
        self._path = self._risolvi_path(path)
        self._dispositivi: dict = {}
        #dizionario che gli pass come chiave l'ID e come valore l'ogetto sensore o attuatore
        self.carica()

    def _risolvi_path(self, path: str) -> Path:
        percorso = Path(path)
        if not percorso.is_absolute():
            percorso = Path(__file__).resolve().parent.parent / percorso
        return percorso

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                dati = json.load(f)
                self._dispositivi = {}
                #faccio un iterazione sulla lista di dizionari caricati dal json
                for d in dati:
                    #controllo il "tipo" per instanziare l'oggetto corretto
                    if d.get("tipo") == "sensore":
                        disp = Sensore.fromDict(d)
                        self._dispositivi[disp.getId()] = disp
                    elif d.get("tipo") == "attuatore":
                        disp = Attuatore.fromDict(d)
                        self._dispositivi[disp.getId()] = disp

        except (FileNotFoundError, json.JSONDecodeError):
            self._dispositivi = {}
    
    def salva(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump([d.toDict() for d in self._dispositivi.values()],f, indent=2, ensure_ascii=False)

    def trovaPerId(self, id_dispositivo: str):
        return self._dispositivi.get(id_dispositivo)

    def aggiungi(self, dispositivo) -> None:
        self._dispositivi[dispositivo.getId()] = dispositivo
        self.salva()

    def tutte(self) -> list:
        return list(self._dispositivi.values())
        
    def elimina(self, id_dispositivo: str) -> None:
        if id_dispositivo in self._dispositivi:
            del self._dispositivi[id_dispositivo] 
            self.salva()
#cosa cambia da backup e dispositovo repository?
