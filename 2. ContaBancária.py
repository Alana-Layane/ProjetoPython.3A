class ContaBancaria:
    def __init__(self, titular, saldo _inicial=0, limite=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if valor > 0 and (self.__saldo + self.__limite) >= valor:
            self.__saldo -= valor
            return True
        return False
    
    def get_saldo(self):
        return self.__saldo
    
    def set_limite(self, novo_limite):
        if novo_limite >= 0:
            self.__limite = novo_limite
            return True
        return False
    
    def __str__(self):
        return (f"Titular: {self.__titular}\n"
                f"Saldo: R${self.__saldo:.2f}\n"
                f"Limite: R${self.__limite:.2f}\n")