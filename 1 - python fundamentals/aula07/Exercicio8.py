# Criar um programa para cadastrar contas bancárias. O programa deve solicitar nome do
# cliente, agência e número da conta. Todas as contas devem iniciar com o saldo zerado. As
# contas devem permitir depósitos e saques. O programa deve ter o seguinte menu:
# 1 - Incluir conta
# 2 - Alterar conta
# 3 - Excluir conta
# 4 - Exibir todas as contas
# 5 - Exibir uma conta
# 6 - Depósito
# 7 - Saque
# 8 - Saldo
# 9 - Histórico (Extrato)
# 10 - Transferência
# 11 - Sair
# Para desenvolvimento desse programa, utilizar o paradigma de orientação à objetos, Lista,
# Estrutura de Repetição e Estrutura de Decisão.


class Pessoa:
    def __init__(self, nome=None, idade=0, saldo=0.0, extrato=""):
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo
        self.__extrato = extrato

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, s):
        self.__saldo = s
        
    @property
    def extrato(self):
        return self.__extrato
    
    @extrato.setter
    def extrato(self, e):
        self.__extrato += "/n" +e
    

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor < self.__saldo:
            print("não foi possivel sacar pois o valor sacado é menor que o saldo")
        else:
            self.__saldo -= valor
        

    def exibirDados(self):
        return f'Nome: {self.__nome} - Saldo:{self.__saldo}'


class PessoaFisica(Pessoa):
    def __init__(self, nome=None, idade=0, cpf='' ,saldo=0.0):
        super().__init__(nome, idade, saldo)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

menu = """
1 - Incluir conta
2 - Alterar conta
3 - Excluir conta
4 - Exibir todas as contas
5 - Exibir uma conta
6 - Depósito
7 - Saque
8 - Saldo
9 - Histórico (Extrato)
10 - Transferência
11 - Sair

Digite a opção desejada: """

pessoas = {
    "11122233344": {
        "nome": "joao",
        "idade": 20
        },
    
    "22233344455" : {
        "nome": "victor",
        "idade": 21
        }
    }


escolha=None
while escolha != 11:
    escolha = int(input(menu))
    match escolha:
        case 1: #inserir
            try:
                nome = input("digite seu nome: ")
                idade = int(input("digite sua idade: "))
                cpf = input("Digite seu CPF")
                x = PessoaFisica(nome, idade, cpf)
                pessoas.append(x)
            except: print("verifique se digitou corretamente")
                
        case 2: #alterar
            cpf=input("Digite o cpf da conta que deseja alterar: ")
            if cpf in pessoas:
                pessoas.pop(cpf)
                nome = input("digite seu nome: ")
                idade = int(input("digite sua idade: "))
                cpf = input("Digite seu CPF")
                

            else:
                print("cpf não localizado")
        
        case 3: #excluir
            cpf=input("Digite o cpf da conta que deseja excluir: ")
            if cpf in pessoas:
                pessoas.pop(cpf)
            else:
                print("cpf não localizado")
                
        case 4: 
            for i in pessoas:
                print(i.exibirDados())
        case 5: 
            cpf=input("Digite o cpf da conta que deseja visualizar: ")
            if cpf in pessoas:
                print(f"\nnome : {pessoas[cpf]["nome"]}\ncpf : {cpf}\nidade : {pessoas[cpf]["idade"]}\n{"*"*30}")
            else:
                print("cpf não localizado")
        case 6: 
            pass
        case 7: 
            pass
        case 8: 
            pass
        case 9: 
            pass
        case 10: 
            pass
        case 11: 
            pass
        case _: 
            break
        
print("\nfim do programa")