class Cliente:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.extrato = []
    
    def atualizar_saldo(self, new_saldo):
        self.saldo = new_saldo
    
    def atualizar_extrato(self, new_change):
        self.extrato.append(new_change)