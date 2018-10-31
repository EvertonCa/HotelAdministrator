import os
import pickle
import Model.Funcionarios
import Model.Cliente
import Model.Quarto
import Utilities.LES
import Utilities.AVL


diretorio_atual = os.getcwd()
diretorio_files = diretorio_atual[:-4]
diretorio_files += 'Files/'


def inicialFuncionario():
    admin = Model.Funcionarios.Funcionario('admin', 'admin', True)
    avl_funcionarios = Utilities.AVL.AVL()
    avl_funcionarios.insert(admin)
    with open(diretorio_files + 'Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(avl_funcionarios, file_output, -1)


def inicialCliente():
    cliente = Model.Cliente.Cliente('Nome', 'telefone', 'cpf', 'endereco', 'sexo')
    avl_clientes = Utilities.AVL.AVL()
    avl_clientes.insert(cliente)
    with open(diretorio_files + 'Clientes.pkl', 'wb') as file_output:
        pickle.dump(avl_clientes, file_output, -1)


def inicialPedidos():
    les_pedidos = Utilities.LES.LES()
    with open(diretorio_files + 'Pedidos.pkl', 'wb') as file_output:
        pickle.dump(les_pedidos, file_output, -1)


def iniciaQuartos(quantidade):
    les_quartos = Utilities.LES.LES()
    for i in range(quantidade):
        quarto = Model.Quarto.Quarto(i+1)
        les_quartos.insert(quarto)
    with open(diretorio_files + 'Quartos.pkl', 'wb') as file_output:
        pickle.dump(les_quartos, file_output, -1)


def salvaFuncionario(funcionario):
    avl_funcionarios = recuperaFuncionarios()
    avl_funcionarios.insert(funcionario)
    with open(diretorio_files + 'Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(avl_funcionarios, file_output, -1)


def salvaPedido(pedido):
    les_pedidos = recuperaPedidos()
    les_pedidos.insert(pedido)
    with open(diretorio_files + 'Pedidos.pkl', 'wb') as file_output:
        pickle.dump(les_pedidos, file_output, -1)


def salvaQuartos(les_quartos):
    with open(diretorio_files + 'Quartos.pkl', 'wb') as file_output:
        pickle.dump(les_quartos, file_output, -1)


def salvaCliente(cliente):
    avl_clientes = recuperaClientes()
    avl_clientes.insert(cliente)
    with open(diretorio_files + 'Clientes.pkl', 'wb') as file_output:
        pickle.dump(avl_clientes, file_output, -1)


def recuperaFuncionarios():
    with open(diretorio_files + 'Funcionarios.pkl', 'rb') as file_input:
        avl_funcionarios = pickle.load(file_input)
    return avl_funcionarios


def recuperaPedidos():
    with open(diretorio_files + 'Pedidos.pkl', 'rb') as file_input:
        les_pedidos = pickle.load(file_input)
    return les_pedidos


def recuperaQuartos():
    with open(diretorio_files + 'Quartos.pkl', 'rb') as file_input:
        les_quartos = pickle.load(file_input)
    return les_quartos


def recuperaClientes():
    with open(diretorio_files + 'Clientes.pkl', 'rb') as file_input:
        avl_clientes = pickle.load(file_input)
    return avl_clientes


# def teste():
#     with open(diretorio_files + 'Funcionarios.pkl', 'rb') as f:
#         funcionarios = pickle.load(f)
#         print(funcionarios.tamanho)
#         print('Usuario: ' + funcionarios.at(0).usuario + ' e Senha: ' + funcionarios.at(0).senha)
#         print('Usuario: ' + funcionarios.at(1).usuario + ' e Senha: ' + funcionarios.at(1).senha)
#     with open(diretorio_files + 'Clientes.pkl', 'rb') as f:
#         les_clientes = pickle.load(f)
#         print(les_clientes.tamanho)
#         print('Nome: ' + les_clientes.at(0).nome + ' e Telefone: ' + les_clientes.at(0).telefone)

def teste():
    with open(diretorio_files + 'Funcionarios.pkl', 'rb') as f:
        avl_funcionarios = pickle.load(f)
        print(avl_funcionarios.tamanho)
        temp = avl_funcionarios.search(avl_funcionarios.raiz, 'admin')
        if temp:
            funcionario = temp.valor
            print('Usuario: ' + funcionario.usuario + ' e Senha: ' + funcionario.senha)
    with open(diretorio_files + 'Clientes.pkl', 'rb') as f:
        avl_clientes = pickle.load(f)
        print(avl_clientes.tamanho)
        temp = avl_clientes.search(avl_clientes.raiz, 'NOME')
        if temp:
            cliente = temp.valor
            print('Nome: ' + cliente.nome + ' e Telefone: ' + cliente.telefone)


# inicialFuncionario()
# inicialCliente()
# func = Model.Funcionarios.Funcionario('fulanildo', '1234567', False)
# salvaFuncionario(func)
# teste()

# print(diretorio_atual)
