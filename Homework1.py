#Ejercicio 1

print("Введите число, чтобы начать игру Pling, Plang, Plong")
num = int(input(""))
print("Введите номер, чтобы закончить игру Pling, Plang, Plong")
ot = int(input(""))

for num in range(num, ot):

    if (num % 7 == 0) and (num % 5 == 0) and (num % 3 == 0):
        print('PlingPlangPlong')
    elif (num % 7 == 0) and (num % 5 == 0):
        print('PlangPlong')
    elif (num % 7 == 0) and (num % 3 == 0):
        print('PlingPlong')
    elif (num % 5 == 0) and (num % 3 == 0):
        print('PlingPlang')
    elif num % 7 == 0:
        print('Plong')
    elif num % 5 == 0:
        print('Plang')
    elif num % 3 == 0:
        print('Pling')
    else:
        print(num)
