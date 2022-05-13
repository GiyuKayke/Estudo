'''
WIKI @classmethod - my abstract

@classmethod 


@staticmethod

'''

from random import randint

class Pessoa:
    ano_atual = 2020
    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
        
    @classmethod 
    def por_ano_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
    
        
#p1 = Pessoa.por_ano_nascimento('Kayke', 1988)

p1 = Pessoa('Luiz', 17)
print(p1.idade)
p1.get_ano_nascimento()
print(p1)
print(p1.idade, p1.nome)
print(Pessoa.gera_id())
print(p1.gera_id())
