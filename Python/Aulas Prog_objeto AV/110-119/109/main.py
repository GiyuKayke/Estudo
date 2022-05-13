from classess import cliente, Endereco

cliente1 = cliente('Luiz',29)
cliente1.add('Belo Horizonte','MG')
cliente1.lista_enderecos()
print('###########################################################################')
del cliente1

cliente2 = cliente('Carlos',49)
cliente2.add('Ouro Preto','MG')
cliente2.lista_enderecos()
print('###########################################################################')


cliente3 = cliente('Kayke',17)
cliente3.add('Guarulhos','SP')
cliente3.lista_enderecos()
print('###########################################################################')

cliente4 = cliente(input('Nome: '),int(input('Idade: ')))
cliente4.add('Belo Horizonte','MG')
cliente4.lista_enderecos()
print('###########################################################################')

