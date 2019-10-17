import getpass

senha = getpass.getpass('Digite sua senha: ')
tentativa = 0
digito = 0

for x in senha:
    digito_i = int(x)
    while digito_i <= 9:
        print(tentativa)      
        if digito_i != tentativa:
            tentativa += 1
        else:
            tentativa = 0
            print('{} Dígito encontrado!'.format(digito_i))
            break
print('Sua senha é {}'.format(senha))