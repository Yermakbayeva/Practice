#Задание 1
for num in range(int(input("Введите число: "))+1):
    if num % 2 == 0:
        print (num)
print("____________________________________________________________________________________")

#Задание 2
number = int(input("Введите число: "))
sum = 0
str = 1
while str <= number:
    sum += str
    str += 1
print ("Сумма всех чисел от 1 до введенного числа:", sum)
print("____________________________________________________________________________________")

#Задание 3
for a in range(0,21,2):
    print ("Четные числа в диапазоне от 0 до 20:", a)
print("____________________________________________________________________________________")

#Задание 4 Таблица умножения
n = int(input("Введите число "))
for b in range (1,11):
    result = n * b
    print ("Результат умножения: ", result)
print("____________________________________________________________________________________")

#Задание 5 Цикл for
for let in "Python":
    print ("Выводим букву: ", let)
print("____________________________________________________________________________________")

#Задание 6 Цикл while
sum = 0
number = 1
while number <= 100:
        sum += number
        number += 2
print (sum)
print("____________________________________________________________________________________")


#Задание 8 Пирамида 
for a in range(1, 10):
    for b in range(a):
        print('*', end=' ')
    print()
print("____________________________________________________________________________________")

#Задание 9 Таблица умножения от 1 до 5
for x in range(1, 10):
    for y in range(1, 6):
        print(x * y, end='\t')
    print()
print("____________________________________________________________________________________")

#Задание 10 Проверка
for b in range(2, int(input("Введите число: ")) + 1):
    number = True
    for t in range(2, int(b**0.5) + 1):
        if b % t == 0:
            number = False
            break
    if number:
        print(f"{b} это число простое.")
    else:
        print(f"{b} это число не относится к простым.")
print("____________________________________________________________________________________")

#Задание со *
for num in range(1,int(input("Введите число: "))+1):
    if num % 2 == 0:
        print ("Четные числа, в диапазоне от 1:", num)

