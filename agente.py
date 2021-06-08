class Agente:

    def __init__(self):
        self.__fila_solicitacoes = []
    
    def adicionar_pedido(self, order):
        self.__fila_solicitacoes.append(order)
    
    def executar_tarefa(self):
        if(len(self.__fila_solicitacoes) != 0):
            self.__fila_solicitacoes[0].executar()
            self.__fila_solicitacoes.pop(0)
        else:
            print("Todas as solicitações já foram realizadas pelo agente.")
        