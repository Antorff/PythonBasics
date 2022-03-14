Ho scritto un programma che mi permette di definire dei conti correnti e di effettuare operazioni fra gli stessi.

Nel file conto1.py ho inserito le classi Conto, ContoCorrente e GestoreContiCorrenti.

1. Conto è una superclasse e mi permette di sfruttare l'ereditarietà per generalizzare il comportamento della sottoclasse ContoCorrente. Utilizza il costruttore __init__ per 

2. ContoCorrente viene utilizzata per definire le varie operazioni sul conto corrente. Ho definito i metodi preleva e deposita e li ho poi utilizzati per andare a modificare il saldo di uno dei due conti. È presente anche un metodo riepilogo che fornisce il resoconto dopo ogni operazione effettuata. Per mantenere privato l'attributo saldo ho utilizzato i decoratori, che consentono di leggerlo e modificarlo in maniera più opportuna. 

3. La classe GestoreContiCorrenti adopera il metodo statico bonifico per prelevare un importo da un conto corrente e depositarlo su un altro. 


Nel file operazioni.py ho importato le classi, definito i conti correnti c1 e c2 ed effettuato le seguenti operazioni:

1. Stampato il riepilogo per visualizzare la situazione "attuale".

2. Utilizzato un ciclo while per permettere ad uno dei due titolari di scegliere se modificare il proprio saldo. Ciò avviene attraverso gli statement if - nel quale viene applicato il metodo saldo - ed elif (per non apportare modifiche). In sostanza, viene prelevata una somma pari al valore del saldo e depositato un nuovo importo.

3. Dopodiché è possibile fornire in input un importo da utilizzare per effettuare un bonifico da un conto corrente all'altro. Se l'importo è maggiore del saldo, il programma chiederà di inserire un valore congruo.  

Al termine viene ristampata la nuova situazione dei conti correnti.
