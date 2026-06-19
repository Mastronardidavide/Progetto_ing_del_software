___________________________________________________________________________________________________________________________________________________
COMPONENTI AGGIUNTIVI DA SCARICARE: 
pyQt6
come scaricare: 
- sul terminale di windows: basta digitare py -m pip install PyQt6 in una posizione qualsiasi
- sul terminale di VsCode: basta digitare py -m pip install PyQt6
___________________________________________________________________________________________________________________________________________________
COME ESEGUIRE IL PROGRAMMA:
- GUI: all'interno della cartella domOS si trova il file main.py. per eseguire il programma basta eseguire quel file main.
- Terminale: all'interno della cartella domOS si trova il file term_main.py. per eseguire il programma basta eseguire quel file main.
___________________________________________________________________________________________________________________________________________________
COME UTILIZZARE IL PROGRAMMA:
Il sistema appena eseguito il run presenterà una schermata di login, con pulsante di registrazione.

Una volta effettuata la registrazione ed il login, c'è la possibilità di aggiungere, rimuovere e configurare dispositivi, zone, scenari ed account, oltre a visualizzare tramite lista i primi tre di questi.
Le soglie dei sensori devono avere valore compreso tra 0 e 100.
La visualizzazione tramite lista permette di identificare uno specifico dispositivo da associare ad una zona o scenario tramite il proprio Id.

I dati riguardanti i dispositivi verranno salvati periodicamente tramite backup, mentre il log degli errori verrà aggiornato ogni qual volta il sistema presenti un errore.
Il log non è accessibile direttamente dalla schermata o dal terminale, in quanto nel caso un ipotetico cliente riscontri problemi con il sistema, un tecnico dedicato potrà accedere al codice del sistema, emettere una diagnosi ed agire di conseguenza.

Per evitare conflitti nella gestione dispositivi, il software utilizza un sistema di priorità che predilige l'autorità dello scenario sopra quella della zona: se un attuatore è presente sia in scenario che in zona, ed è impostato a due orario di attivazione diversi, in caso questi si dovessero sovrappore, il sistema applica quello dello scenario
