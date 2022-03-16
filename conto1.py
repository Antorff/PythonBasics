#superclasse Conto

class Conto:
    def __init__(self, nome, cognome, conto):
        self.nome = nome
        self.cognome = cognome
        self.conto = conto

#classe ContoCorrente: utilizzo l'ereditarietà per generalizzare il comportamento della sottoclasse

class ContoCorrente(Conto):

    def __init__(self, nome, cognome, conto, importo):
        super().__init__(nome, cognome, conto)
        self.__saldo = importo 

#definisco i metodi preleva e deposita per prelevare o depositare un importo sul saldo:


    def preleva(self, importo):
            self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

#definisco il metodo riepilogo per stampare nome del proprietario, numero del conto e relativo saldo

  #  def riepilogo(self):
  #      print(
  #      "\n Titolare = ", self.nome,self.cognome,
  #      "\n Banca    = ", self.conto,
  #      "\n Saldo    = ", self.__saldo)

    def riepilogo(self):
        dizionario = {
            "Titolare": self.nome+" "+self.cognome,
            "Banca": self.conto,
            "Saldo": self.__saldo
        }
        for i in dizionario:
            print(i,"=", dizionario[i])


#definisco un metodo per permettere ad uno dei titolari di modificare il proprio saldo

    def start(self):
        
        risposta = int(input((self.nome+", "+"se intendi modificare il tuo saldo digita 0, altrimenti digita 1: ")))
        print()

        while(risposta not in [0,1]):
            print("ATTENZIONE: Non sono ammessi numeri diversi da 0 o 1 \n")
            print()
            risposta = int(input((self.nome+", "+"se intendi modificare il tuo saldo digita 0, altrimenti digita 1: ")))
    
        print()

        if(risposta == 0):
            nuovosaldo = int(input(self.nome+", "+"modifica pure il tuo saldo: "))
            self.saldo = nuovosaldo
            print()
            print(self.nome+", "+"il tuo saldo è stato modificato con successo: \n")
            self.riepilogo()
            print()
        elif(risposta == 1):
            print("Hai deciso di non apportare modifiche") 

#Definisco un metodo che consente di effettuare un bonifico da un conto all'altro

    def versamento(self, destinazione):
        scelta = int(input((self.nome+", "+"se intendi effettuare un bonifico digita 0, altrimenti digita 1: ")))
        print()

        while(scelta not in [0,1]):
            print("ATTENZIONE: Non sono ammessi numeri diversi da 0 o 1 \n")
            print()
            scelta = int(input((self.nome+", "+"se intendi effettuare un bonifico  digita 0, altrimenti digita 1: ")))
            print()

        if(scelta == 0):
            importo = int(input(self.nome+", "+"inserisci l'importo del bonifico: "))
            print()
            while(importo > self.saldo):
                print("Non hai abbastanza credito sul conto")
                print()
                importo = int(input(self.nome+", "+"Inserisci l'importo del bonifico: "))
                print()
            GestoreContiCorrenti.bonifico(self, destinazione, importo)
            print(self.nome+", "+"il tuo bonifico è stato effettuato con successo. Ecco il tuo nuovo saldo: \n")
            print()
            self.riepilogo()
            print()            
        elif(scelta == 0):
            print("Hai deciso di non effettuare nessun versamento")
            print()        
    
       

#utilizzo i decoratori per leggere il saldo attuale e modificarlo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

#definisco la classe GestoreContiCorrenti

class GestoreContiCorrenti:

#definisco il metodo statico bonifico che permette di trasferire un importo fra due conti correnti

    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)