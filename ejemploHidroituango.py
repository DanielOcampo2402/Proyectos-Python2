

nivelAgua = int(input('Digite el nivel del agua : '))

if(nivelAgua<200):
    print('Hay muy poca agua en la empresa')
elif(nivelAgua>=200 and nivelAgua < 450):
    print('Todo esta perfecto')
else :
    print('¡PELIGRO!, el nivel del agua es superior a 450m')   
