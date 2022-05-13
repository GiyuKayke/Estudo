'''
ㅤｋａｙｋｅㅤ https://github.com/GiyuKayke

Este progama consiste em pegar uma rede é testar os ping dele pode ser utilizada da forma 
,como bem entender

kaykesandesg@gmail.com
'''




import os # Importa o módulo ou biblioteca os (integrantes as programas e #recursos do do S.O)

print('#'*178)#imprime # 178 vezes
ip_ou_host = input("digite o Ip ou a host a ser verificada: ")
#criamos uma variavel que vai receber do usuario um io
print("'" * 178) ##imprmindo ' 178 vezes 
os.system('ping -n 6 {}' .format(ip_ou_host)) #chamando sytem da bliblioteca or - comando ping 
#-n -num de pacotes quimpore serão e {}
print("'" * 178) 
