# Elección aleatoria Maquina
import random

# function randint(min,max)
rand_int = random.randint(1, 3)
if rand_int == 1:
    choice_maq = 'Piedra'
elif rand_int == 2:
    choice_maq = 'Papel'
else:
    choice_maq = 'Tijeras'

# Elección de usuario
choice_text = '''
Escribe una de las siguientes opciones:
    Piedra
    Papel
    Tijera
'''
choice_user = input(choice_text)

#Impresión de opciones
print('Selección del Usuario --->', choice_user)
print('Selección de la Máquina --->', choice_maq)

# Ganador!
if choice_maq == choice_user:
    print("¡EMPATE!")
else:
    if choice_maq == 'Piedra' and choice_user == 'Papel':
        print('¡GANÓ EL USUARIO!')
    elif choice_maq == 'Piedra' and choice_user == 'Tijeras':
        print('¡GANÓ LA MÁQUINA!')
    elif choice_maq == 'Papel' and choice_user == 'Tijeras':
        print('¡GANÓ EL USUARIO!')
    elif choice_maq == 'Papel' and choice_user == 'Piedra':
        print('¡GANÓ LA MÁQUINA!')
    elif choice_maq == 'Tijeras' and choice_user == 'Piedra':
        print('¡GANÓ LA USUARIO!')
    else:
        print('¡GANÓ EL USUARIO!')