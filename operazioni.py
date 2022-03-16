import string
from conto1 import ContoCorrente

from conto1 import GestoreContiCorrenti
print()
print("SITUAZIONE PRECEDENTE:")       

#definisco i conti correnti c1 e c2

c1 = ContoCorrente("Antonio","Raffa","Intesa",5000)
c2 = ContoCorrente("Maria","Rossi","Unicredit",15000)

#stampo le informazioni relative a c1 e c2
print()
c1.riepilogo()
print()
c2.riepilogo()
print()

#Posso decidere di modificare il suo saldo o di lasciarlo invariato:

c1.start()
print()
c2.start()
print()



#Uno dei due utenti fa un bonifico all'altro:

c1.versamento(c2)
print()
c2.versamento(c1)

#ristampo le informazioni relative ai due conti correnti per visualizzare le modifiche apportate
print()
print("SITUAZIONE ATTUALE:")       
print()
c1.riepilogo()
print()
c2.riepilogo()