'''
Public       _  dentro e fora da classe
protected    _  dentro da classe ou filha  _
private      _  so esta dentro da classe   __
'''





class Base_d_dados:
    def __init__(self):
        self._dados = {}
        
    def inserir_cliente(self, id, nome):
        if 'cliente' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})
    def list(self):                                          # ERRO D ALGUM COISA TENTA VER AI OQ DEU 
        for id, nome in dados.item():                        #    for id, nome in dados.item()
            print(id, nome)                                                 # NameError: name 'dados' is not defined  

#    def del_client(self, id):
#        del self.dados['clientes'] [id]    


bd = Base_d_dados()
bd.inserir_cliente(1,'Pedro')     
bd.inserir_cliente(2,'Matheus')     
bd.inserir_cliente(3,'José')     
#bd.del_client(2)
bd.list()

