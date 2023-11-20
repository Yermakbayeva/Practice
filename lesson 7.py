#Функция для вычисления факториала числа
def fact(n): 
    if n==1 or n==0:
     return 1 
    else: return n*fact(n-1) 

n=int(input("Введите ваше число: "))
print("Факториал введенного числа",n,"равен: ",fact(n))

# Функция для нахождения наибольшего общего делителя (НОД) двух чисел
def NOD(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для нахождения НОК двух чисел
def NOK(a, b):
    return (a * b) // NOD(a, b)

x1 = int(input("Введите первое число: "))
x2 = int(input("Введите второе число: "))

res = NOK(x1, x2)
print(f"Наименьшее общее кратное {x1} и {x2} равно {res}")

def temp(tc):
    for i in range(tc):
        tf = (9 / 5) * tc + 32
    return tf
 
 # Функция для перевода с Цельсия в Фаренгейт
def main():
    tc = int(input('Введите температуру по Цельсию: '))
    while tc >= -273:
        tf = temp(tc)
        print('Температура Цельсия', tc, 'равна', tf, 'градусам Фаренгейта.')
        tc = int(input('Введите температуру по Цельсию: '))
 
main()