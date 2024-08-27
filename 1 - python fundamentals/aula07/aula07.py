class Pessoa:
    def __init__(self, telefone, idade, nome, saldo) -> None:
        self.__nome = None
        self.__telefone = None
        self.__idade = None
        self.__saldo = None
        
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
        self.saldo = saldo
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
        
        
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
    def saldo(self, saldo):
        self.__saldo = saldo
        
class PessoaFisica(Pessoa):
    def __init__(self, telefone, idade, nome, saldo,cpf) -> None:
        super().__init__(telefone, idade, nome, saldo)
        
        self.__cpf = None
        
    
p1 = Pessoa(1111, 15)
print(p1.idade)

p1.idade=3
print(p1.idade)
