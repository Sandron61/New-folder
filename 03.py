class Pessoa:
    nome = "Sandron"
    idade = 19
    altura = 1.90
    peso = 70
    @classmethod
    def descrever(cls):
        return f"Nome:{cls.nome}, Idade:{cls.idade}, Altura:{cls.altura}, Peso:{cls.peso}"
    @classmethod
    def envelhecer(cls):
        cls.idade = cls.idade + 1

Pessoa.envelhecer()
print(Pessoa.idade)