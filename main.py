from cliente import Cliente
from servicos import *
from agente import Agente

# cliente criado
cliente = Cliente("Davi", 200)

# serviços demandados pelo cliente
servico = Servico(cliente)

saldo_inicial = Saldo(servico)
transferencia1 = Transferencia(servico, 10)
transferencia2 = Transferencia(servico, 50)
extrato = Extrato(servico)
saldo_final = Saldo(servico)

# agente adiciona os servicos a serem efetuados
agente = Agente()
agente.adicionar_pedido(saldo_inicial)
agente.adicionar_pedido(transferencia1)
agente.adicionar_pedido(transferencia2)
agente.adicionar_pedido(extrato)
agente.adicionar_pedido(saldo_final)

# realizacao dos servicos
print("------ execução dos servicos --------\n")
agente.executar_tarefa()
agente.executar_tarefa()
agente.executar_tarefa()
agente.executar_tarefa()
agente.executar_tarefa()
agente.executar_tarefa()
print("------ fim dos servicos ------\n")