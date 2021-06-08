from abc import ABC, abstractmethod

class Order(ABC):

    @abstractmethod
    def executar(self):
        pass

class Transferencia(Order):

    def __init__(self, servico, valor):
        self.servico = servico
        self.valor = valor
    
    def executar(self):
        self.servico.transferencia(self.valor)
    
class Extrato(Order):

    def __init__(self, servico):
        self.servico = servico
    
    def executar(self):
        self.servico.extrato()

class Saldo(Order):

    def __init__(self, servico):
        self.servico = servico
    
    def executar(self):
        self.servico.saldo()

class Servico:

    def __init__(self, cliente):
        self.cliente = cliente
    
    def transferencia(self, valor):
        print("- TRANSFERÊNCIA:")
        if(self.cliente.saldo >= valor):
            self.cliente.atualizar_saldo(self.cliente.saldo - valor)
            self.cliente.atualizar_extrato(f"Transferencia de {valor}, em reais")
            print("Transferência realizada.\n")
        else:
            print("O cliente não possui saldo suficiente para realizar a transferência.\n")

    def extrato(self):
        print("- EXTRATO: Segue seu extrato:\n")
        for change in self.cliente.extrato:
            print(change, "\n")
    
    def saldo(self):
        print("- SALDO: Seu saldo é de ", self.cliente.saldo, "\n")
