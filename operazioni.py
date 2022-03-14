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


risposta = int(input(("Antonio, se intendi modificare il tuo saldo digita 0, altrimenti digita 1: ")))

while(risposta not in [0,1]):
    print("ATTENZIONE: Non sono ammessi numeri diversi da 0 o 1 \n")
    print()
    risposta = int(input(("Antonio, se intendi modificare il tuo saldo digita 0, altrimenti digita 1: ")))
    
print()

if(risposta == 0):
    nuovosaldo = int(input("Antonio, modifica pure il tuo saldo: "))
    c1.saldo = nuovosaldo
    print()
    print("Il tuo saldo è stato modificato con successo: \n")
    c1.riepilogo()
    print()
elif(risposta == 1):
    print("Hai deciso di non apportare modifiche")  

print()



#Antonio fa un bonifico a Maria

importo = int(input("Inserisci l'importo del bonifico: "))
print()
while(importo > c1.saldo):
    print("Non hai abbastanza credito sul conto")
    print()
    importo = int(input("Inserisci l'importo del bonifico per Maria: "))
    
GestoreContiCorrenti.bonifico(c1, c2, importo)

#ristampo le informazioni relative ai due conti correnti per visualizzare le modifiche apportate
print()
print("SITUAZIONE ATTUALE:")       
print()
c1.riepilogo()
print()
c2.riepilogo()