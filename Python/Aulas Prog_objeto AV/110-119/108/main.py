from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Vibrador',120)
p2 = Produto('Camisinha',20)
p3 = Produto('Plug anal', 70)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()                
print(carrinho.soma_total())