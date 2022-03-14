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
       