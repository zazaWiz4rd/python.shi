"""
descripción: Mostrar per pantalla un quadrat de mida N (la triarà l'usuari)
"""
num = int(input())
obj = "#"

for i in range(1, num + 1):
    if i == 1 or i == num:
        print(num * obj)
    else:
        print(obj + " " * (num - 2) + obj)