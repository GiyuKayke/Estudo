class carrinho_de_compra:
    def __init__(self):
        self.produto = []
    
    def inserir_produtos(self,produto):
        self.produto.append(produto)
    
    def list_produto(self):
        for produto in self.produto:
            print(produto.nome,produto.valor)
    
    def soma_total(self):
        for produto in self.produto:
            total += produto.valor
        return total
    
    
class Produto:
    def __init__(self, nome, valor):
       self.nome = nome
       self.valor = valor 
