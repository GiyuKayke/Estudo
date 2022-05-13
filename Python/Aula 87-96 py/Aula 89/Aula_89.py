file = open('Dado.txt',"w+")

file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

file.seek(0, 0)
print('Lendo Linhas: ')
print(file.read())
print('##################')

file.seek(0,0)
print(file.readline(), end = '')
print(file.readline(), end = '')
print(file.readline(), end = '')

print('##################')

file.seek(0,0)
for linha in file.readlines():
    print(linha,end='')

print('##################')

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

print('##################')



file.close()


with open('Dado.txt', 'w+') as file:
    file.write('Outra linha ')
    file.seek(0)
    
    print(file.read())
    
import os
os.remove('dado.txt')


import json 
d1 = {
    'Pessoa 1' : {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2' : {
        'nome': 'maria',
        'idade': 19,
    },
    'Pessoa 3' : {
        'nome': 'Kayke',
        'idade': 17,
    },
}

d1_json =  json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
