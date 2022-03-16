Ho scritto un programma che mi permette di definire dei conti correnti e di effettuare operazioni fra gli stessi.

Nel file conto1.py ho inserito le classi Conto, ContoCorrente e GestoreContiCorrenti.

1. Conto è una superclasse e mi permette di sfruttare l'ereditarietà per generalizzare il comportamento della sottoclasse ContoCorrente. Utilizza il costruttore __init__ per 

2. ContoCorrente viene utilizzata per definire le varie operazioni sul conto corrente. Ho definito i metodi preleva e deposita e li ho poi utilizzati per andare a modificare il saldo di uno dei due conti. I metodi start e versamento consentono rispettivamente di modificare il saldo (viene prelevata una somma pari al valore del saldo e depositato un nuovo importo) ed effettuare un bonifico. In particolare, viene chiesto all'utente se intende effettuare le due operazioni tramite un ciclo while e gli statement if ed elif. È presente anche un metodo riepilogo che fornisce il resoconto dopo ogni operazione effettuata. Per mantenere privato l'attributo saldo ho utilizzato i decoratori, che consentono di leggerlo e modificarlo in maniera più opportuna. 

3. La classe GestoreContiCorrenti adopera il metodo statico bonifico per prelevare un importo da un conto corrente e depositarlo su un altro. 


Nel file operazioni.py ho importato le classi, definito i conti correnti c1 e c2 ed effettuato le seguenti operazioni:

1. Stampato il riepilogo per visualizzare la situazione "attuale".

2. Ho richiamato i metodi start e versamento sui due conti correnti per consentire agli utenti di effettuare le operazioni.

3. Al termine viene stampata la nuova situazione dei conti correnti.
