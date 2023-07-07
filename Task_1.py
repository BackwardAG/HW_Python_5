'''Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

def numApowB(a, b):
    if b == 0:
        return 1
    return a * numApowB(a, b - 1)

a = int(input('Enter a number: '))
b = int(input('Enter a power: '))
print(numApowB(a, b))   