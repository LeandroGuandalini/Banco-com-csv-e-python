from util import *

def consultar_contas(contas):
    for conta in contas:
        print(conta[0], conta[1], conta[2])
    print()

def consultar_conta(contas):
    id = entrar_id()
    conta = pesquisar_conta(contas, id)
    if (not conta): #(conta == []):
        print("Erro: conta não existe")
        return
    print(conta)

def incluir_conta(contas):
    id = entrar_id()
    conta_pesquisada = pesquisar_conta(contas, id)
    if (conta_pesquisada):
        print("Erro: conta já existe")
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    conta = [id, nome, saldo]
    contas.append(conta)

def excluir_conta(contas):
    id = entrar_id()
    conta_pesquisada = pesquisar_conta(contas, id)
    if (not conta_pesquisada):
        print("Erro: conta não existe")
        return
    contas.remove(conta_pesquisada)

def alterar_conta(contas):
    id = entrar_id()
    conta= pesquisar_conta(contas, id)
    if (not conta):
        print("Erro: conta não existe")
        return
    oper = entrar_operacao()
    valor = entrar_valor()
    if (oper == "C"):
        conta[2] += valor
    else:
        conta[2] -= valor
