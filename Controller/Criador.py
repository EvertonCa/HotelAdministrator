import os
import pickle
import Model.Funcionarios
import Model.Cliente

diretorio_atual = os.getcwd()
diretorio_files = diretorio_atual[:-10]
diretorio_files += 'Files/'


def recuperaFuncionarios():
    with open(diretorio_files + 'Funcionarios.pkl', 'rb') as file_input:
        funcionarios = pickle.load(file_input)
    return funcionarios


def recuperaClientes():
    with open(diretorio_files + 'Clientes.pkl', 'rb') as file_input:
        clientes = pickle.load(file_input)
    return clientes


def salvaFuncionario(funcionario):
    funcionarios = recuperaFuncionarios()
    funcionarios.append(funcionario)
    with open(diretorio_files + 'Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(funcionarios, file_output, -1)


def salvaCliente(cliente):
    clientes = recuperaClientes()
    clientes.append(cliente)
    with open(diretorio_files + 'Clientes.pkl', 'wb') as file_output:
        pickle.dump(clientes, file_output, -1)


def inicialFuncionario():
    admin = Model.Funcionarios.Funcionario('admin', 'admin', True)
    funcionarios = [admin]
    with open(diretorio_files + 'Funcionarios.pkl', 'wb') as file_output:
        pickle.dump(funcionarios, file_output, -1)


def inicialCliente():
    cliente = Model.Cliente.Cliente('Nome', 'telefone', 'cpf', 'endereco', 'sexo')
    clientes = [cliente]
    with open(diretorio_files + 'Clientes.pkl', 'wb') as file_output:
        pickle.dump(clientes, file_output, -1)


def teste():
    with open(diretorio_files + 'Funcionarios.pkl', 'rb') as f:
        funcionarios = pickle.load(f)
        print(len(funcionarios))
        print('Usuario: ' + funcionarios[0].usuario + ' e Senha: ' + funcionarios[0].senha)
    with open(diretorio_files + 'Clientes.pkl', 'rb') as f:
        clientes = pickle.load(f)
        print(len(clientes))
        print('Nome: ' + clientes[0].nome + ' e Telefone: ' + clientes[0].telefone)


inicialFuncionario()
inicialCliente()
teste()
#func = Model.Funcionarios.Funcionario('fulanildo', '1234567', False)
#salvaFuncionario(func)
#teste()
