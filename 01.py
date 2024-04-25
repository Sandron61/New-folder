class Pessoa:
    def __init__(self, entrada1, entrada2, entrada3, entrada4):
        self.nome = entrada1
        self.idade = entrada2
        self.peso = entrada3
        self.sexo = entrada4
    def saudar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
    def descrever(self):
        print(f"Nome:{self.nome},Idade:{self.idade},Peso:{self.peso},Sexo:{self.sexo}")

pessoa = Pessoa("Sandron",19,70,"masculino")
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.peso)
print(pessoa.sexo)
pessoa.saudar()
pessoa.descrever()