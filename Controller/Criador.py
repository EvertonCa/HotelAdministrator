import os
import pickle
import Model.Funcionarios
import Model.Cliente
import Utilities.LES

diretorio_atual = os.getcwd()
diretorio_files = diretorio_atual[:-10]
diretorio_files += 'Files/'


def recuperaFuncionarios():
    with open(diretorio_files + 'Funcionarios.pkl', 'rb') as file_input:
        les_funcionarios = pickle.load(file_input)
    return les_funcionarios


def recuperaClientes():
    with open(diretorio_files + 'Clientes.pkl', 'rb') as file_input:
        les_clientes = pickle.load(file_input)
    return les_clientes


def salvaFuncionario(funcionario):
    les_funcionarios = recuperaFuncionarios()
    les_funcionarios.insert(funcionario)
    with open(diretorio_files + 'Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(les_funcionarios, file_output, -1)


def salvaCliente(cliente):
    les_clientes = recuperaClientes()
    les_clientes.append(cliente)
    with open(diretorio_files + 'Clientes.pkl', 'wb') as file_output:
        pickle.dump(les_clientes, file_output, -1)


def inicialFuncionario():
    admin = Model.Funcionarios.Funcionario('admin', 'admin', True)
    les_funcionarios = Utilities.LES.LES()
    les_funcionarios.insert(admin)
    with open(diretorio_files + 'Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(les_funcionarios, file_output, -1)


def inicialCliente():
    cliente = Model.Cliente.Cliente('Nome', 'telefone', 'cpf', 'endereco', 'sexo')
    les_clientes = Utilities.LES.LES()
    les_clientes.insert(cliente)
    with open(diretorio_files + 'Clientes.pkl', 'wb') as file_output:
        pickle.dump(les_clientes, file_output, -1)


def teste():
    with open(diretorio_files + 'Funcionarios.pkl', 'rb') as f:
        funcionarios = pickle.load(f)
        print(funcionarios.tamanho)
        print('Usuario: ' + funcionarios.at(0).usuario + ' e Senha: ' + funcionarios.at(0).senha)
        print('Usuario: ' + funcionarios.at(1).usuario + ' e Senha: ' + funcionarios.at(1).senha)
    with open(diretorio_files + 'Clientes.pkl', 'rb') as f:
        les_clientes = pickle.load(f)
        print(les_clientes.tamanho)
        print('Nome: ' + les_clientes.at(0).nome + ' e Telefone: ' + les_clientes.at(0).telefone)


#inicialFuncionario()
inicialCliente()
# func = Model.Funcionarios.Funcionario('fulanildo', '1234567', False)
# salvaFuncionario(func)
teste()
