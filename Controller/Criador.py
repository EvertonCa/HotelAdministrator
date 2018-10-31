import os
import pickle
import Model.Funcionarios
import Model.Cliente
import Model.Quarto
import Utilities.LES
import Utilities.AVL
import Utilities.Fila


os.chdir('./Files/')
diretorio_files = os.getcwd()


def inicialFuncionario(diretorio=diretorio_files):
    admin = Model.Funcionarios.Funcionario('admin', 'admin', True)
    avl_funcionarios = Utilities.AVL.AVL()
    avl_funcionarios.insert(admin)
    with open(diretorio + '/Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(avl_funcionarios, file_output, -1)


def inicialCliente(diretorio=diretorio_files):
    cliente = Model.Cliente.Cliente('Nome', 'telefone', 'cpf', 'endereco', 'sexo')
    avl_clientes = Utilities.AVL.AVL()
    avl_clientes.insert(cliente)
    with open(diretorio + '/Clientes.pkl', 'wb') as file_output:
        pickle.dump(avl_clientes, file_output, -1)


def inicialPedidos(diretorio=diretorio_files):
    les_pedidos = Utilities.LES.LES()
    with open(diretorio + '/Pedidos.pkl', 'wb') as file_output:
        pickle.dump(les_pedidos, file_output, -1)


def iniciaQuartos(quantidade, diretorio=diretorio_files):
    les_quartos = Utilities.LES.LES()
    for i in range(quantidade):
        quarto = Model.Quarto.Quarto(i+1)
        les_quartos.insert(quarto)
    with open(diretorio + '/Quartos.pkl', 'wb') as file_output:
        pickle.dump(les_quartos, file_output, -1)


def iniciaSenhas(diretorio=diretorio_files):
    fila_senhas_prioritarias = Utilities.Fila.FilaEncadeada()
    fila_senhas_normais = Utilities.Fila.FilaEncadeada()
    with open(diretorio + '/SenhasNormais.pkl', 'wb') as file_output:
        pickle.dump(fila_senhas_normais, file_output, -1)
    with open(diretorio + '/SenhasPrioritarias.pkl', 'wb') as file_output:
        pickle.dump(fila_senhas_prioritarias, file_output, -1)


def salvaFuncionario(funcionario, diretorio=diretorio_files):
    avl_funcionarios = recuperaFuncionarios()
    avl_funcionarios.insert(funcionario)
    with open(diretorio + '/Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(avl_funcionarios, file_output, -1)


def salvaPedido(pedido, diretorio=diretorio_files):
    les_pedidos = recuperaPedidos()
    les_pedidos.insert(pedido)
    with open(diretorio + '/Pedidos.pkl', 'wb') as file_output:
        pickle.dump(les_pedidos, file_output, -1)


def salvaQuartos(les_quartos, diretorio=diretorio_files):
    with open(diretorio + '/Quartos.pkl', 'wb') as file_output:
        pickle.dump(les_quartos, file_output, -1)


def salvaCliente(cliente, diretorio=diretorio_files):
    avl_clientes = recuperaClientes()
    avl_clientes.insert(cliente)
    with open(diretorio + '/Clientes.pkl', 'wb') as file_output:
        pickle.dump(avl_clientes, file_output, -1)


def salvaSenhaNormal(senha, diretorio=diretorio_files):
    fila_senhas_normais = recuperaSenhasNormais()
    fila_senhas_normais.push(senha)
    with open(diretorio + '/SenhasNormais.pkl', 'wb') as file_output:
        pickle.dump(fila_senhas_normais, file_output, -1)


def salvaSenhaPrioritaria(senha, diretorio=diretorio_files):
    fila_senhas_prioritarias = recuperaSenhasNormais()
    fila_senhas_prioritarias.push(senha)
    with open(diretorio + '/SenhasPrioritarias.pkl', 'wb') as file_output:
        pickle.dump(fila_senhas_prioritarias, file_output, -1)


def recuperaFuncionarios(diretorio=diretorio_files):
    with open(diretorio + '/Funcionarios.pkl', 'rb') as file_input:
        avl_funcionarios = pickle.load(file_input)
    return avl_funcionarios


def recuperaPedidos(diretorio=diretorio_files):
    with open(diretorio + '/Pedidos.pkl', 'rb') as file_input:
        les_pedidos = pickle.load(file_input)
    return les_pedidos


def recuperaQuartos(diretorio=diretorio_files):
    with open(diretorio + '/Quartos.pkl', 'rb') as file_input:
        les_quartos = pickle.load(file_input)
    return les_quartos


def recuperaClientes(diretorio=diretorio_files):
    with open(diretorio + '/Clientes.pkl', 'rb') as file_input:
        avl_clientes = pickle.load(file_input)
    return avl_clientes


def recuperaSenhasNormais(diretorio=diretorio_files):
    with open(diretorio + '/SenhasNormais.pkl', 'rb') as file_input:
        fila_senhas_normais = pickle.load(file_input)
    return fila_senhas_normais


def recuperaSenhasPrioritarias(diretorio=diretorio_files):
    with open(diretorio + '/SenhasPrioritarias.pkl', 'rb') as file_input:
        fila_senhas_prioritarias = pickle.load(file_input)
    return fila_senhas_prioritarias


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

def teste(diretorio=diretorio_files):
    with open(diretorio + '/Funcionarios.pkl', 'rb') as f:
        avl_funcionarios = pickle.load(f)
        print(avl_funcionarios.tamanho)
        temp = avl_funcionarios.search(avl_funcionarios.raiz, 'admin')
        if temp:
            funcionario = temp.valor
            print('Usuario: ' + funcionario.usuario + ' e Senha: ' + funcionario.senha)
    with open(diretorio + '/Clientes.pkl', 'rb') as f:
        avl_clientes = pickle.load(f)
        print(avl_clientes.tamanho)
        temp = avl_clientes.search(avl_clientes.raiz, 'NOME')
        if temp:
            cliente = temp.valor
            print('Nome: ' + cliente.nome + ' e Telefone: ' + cliente.telefone)
        temp = avl_clientes.search(avl_clientes.raiz, 'ghjnb')
        if temp:
            cliente = temp.valor
            print('Nome: ' + cliente.nome + ' e Telefone: ' + cliente.telefone)


# inicialFuncionario()
# inicialCliente()
# func = Model.Funcionarios.Funcionario('fulanildo', '1234567', False)
# salvaFuncionario(func)
# cliente = Model.Cliente.Cliente('ghjnb', 'vfghj', 'vfghj', 'vghjn', 'vfgh')
# salvaCliente(cliente)
# teste()
