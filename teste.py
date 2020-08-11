class Pessoa():
    def __init__(self):
        self.pessoa = 'Tiago'

    def sobrenome(self):
        self.pessoa = self.pessoa + ' de Souza'
        return self

    def idade(self):
        self.pessoa = self.pessoa + ' idade: 29'
        return self

    def nacionalidade(self):
        self.pessoa = self.pessoa + ' nacionalide: Brasileiro'
        return self


pessoa = Pessoa()
pessoa.sobrenome()
print(pessoa.pessoa)
