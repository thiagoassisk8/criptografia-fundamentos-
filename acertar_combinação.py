
import getpass
import random
import time
senha = getpass.getpass("Digite sua senha em números com 6 caracteres: ")

'''o método [] não consegue selecionar os indices dos números, 
por isso coloquei o int depois do while para fazer a conversão
de string para inteiro apos os carecters terem sido selecionados
'''
n1 = random.randint(0,9)
while int(senha[0]) != n1:
    n1 = random.randint(0,9)
    time.sleep(0.5)
    print(n1)
    if int(senha[0]) == n1:
        print('Primeiro Digito {}'.format(n1))
        #break

n2 = random.randint(0,9)
while int(senha[1]) != n2:
    n2 = random.randint(0,9)
    time.sleep(0.5)
    print(n2)
    if int(senha[1]) == n2:
        print('Segundo Digito {}'.format(n2))
        #break

n3 = random.randint(0,9)
while int(senha[2]) != n3:
    n3 = random.randint(0,9)
    time.sleep(0.5)
    print(n3)
    if int(senha[2]) == n3:
        print('Terceiro Digito {}'.format(n3))
        #break

n4 = random.randint(0,9)
while int(senha[3]) != n4:
    n4 = random.randint(0,9)
    time.sleep(0.5)
    print(n4)
    if int(senha[3]) == n4:
        print('Quarto Digito {}'.format(n4))
        #break

n5 = random.randint(0,9)
while int(senha[4]) != n5:
    n5 = random.randint(0,9)
    time.sleep(0.5)
    print(n5)
    if int(senha[4]) == n5:
        print('Quinto Digito {}'.format(n5))
        #break

n6 = random.randint(0,9)
while int(senha[5]) != n6:
    n6 = random.randint(0,9)
    time.sleep(0.5)
    print(n6)
    if int(senha[5]) == n6:
        print('Sexto Digito {}'.format(n6))
        #break


print('Sua senha é {}{}{}{}{}{}'.format(n1,n2,n3,n4,n5,n6))
