class Pessoa:

    def __init__(self, entrada1, entrada2, entrada3, entrada4):
        self.nome = entrada1
        self.idade = entrada2
        self.altura = entrada3
        self.peso = entrada4
    def comparar(self,outra):
        if self.idade <= outra.idade:
            outra.idade - self.idade
        else:
            self.idade - outra.idade

Pessoa1= Pessoa("Alberto", 340, 1,95, 10)
Pessoa2 = Pessoa("Bernardo", 27, 1,70, 60)
diferenca = Pessoa1.comparar(Pessoa2)
print("A diferença de idade entre {} e {} é de {} anos.".format(Pessoa1.nome, Pessoa2.nome,diferenca))
