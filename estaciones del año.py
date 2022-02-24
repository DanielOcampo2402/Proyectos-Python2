
'''

mesAño = int(input('Digite un mes del año(en numeros del 1-12) : '))

if(mesAño == 1 or mesAño == 2 or mesAño == 3):
    print(f'Estamos en la estacion de invierno en el mes de: {mesAño}')
elif(mesAño == 4 or mesAño == 5 or mesAño == 6):
    print(f'Estamos en la estacion de verano en el mes de: {mesAño} ')
elif(mesAño == 7 or mesAño == 8 or mesAño == 9):
    print(f'Estamos en la estacion de otoño en el mes de: {mesAño}')    
elif(mesAño == 10 or mesAño == 11 or mesAño == 12):
    print(f'Estamos en la estacion de primavera en el mes de: {mesAño}')
else:
    print('Digitaste un numero diferente del 1-12')      

'''

cont = 0
while(cont < 10):
    cont += 1
    print(cont)
print("Termino el ciclo")