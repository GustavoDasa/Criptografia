import random as rd
menu = '\n>>>> Cripto <<<<\n\n1-Criptografar\n2-Descriptografar'
arquivo = 'mensagem.py'
exec(open(arquivo).read())

def Crip():
    rd.seed(int(input('\nInsira a senha: ')))
    x = input('\nInsira uma mensagem: ').upper()
    lista = []
    y = ''
    for i in x:
      lista.append(ord(i))
    for i in lista:
      y += chr(i+rd.randint(0,5))
      with open(arquivo, 'w+') as arq:
          arq.writelines(['y = "',y,'"'])


def Desc():

    rd.seed(int(input('\nInsira a senha: ')))
    print()
    lista = []
    for i in y:
      lista.append(ord(i))
    for i in lista:
      print(chr(i-rd.randint(0,5)).lower() ,end='')


print(menu)
op = int(input('\nEscolha uma opção: '))

if op == 1:
  Crip()
elif op ==2:
  Desc()