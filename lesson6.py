#Задание 1
eva = int(input("Введите вашу оценку от 1 до 10: "))
if eva >= 1 and eva <= 3:
    print ("Увы, ваша оценка - плохо")
else:
    if eva >= 4 and eva <= 6:
      print ("Ваша оценка - удовлетворительно")
    else:
     if eva >= 7 and eva <= 9:
         print("Ваша оценка - хорошо")
     else:
        print ("Ваша оценка - отлично")
print("_____________________________________________________________")

#Задание 2
time = int(input("Введите текущее время: "))
if time >= 6 and time <= 12:
    print ("Доброе утро!")
else:
    if time > 12 and time <= 18:
      print ("Добрый день!")
    else:
       if time > 18 and time <= 24:
         print("Добрый вечер!")
       elif time >=0 and time < 6:
          print ("Доброй ночи!")
       else:
         print ("Введенное время неверно!")
print("_____________________________________________________________")

size = 7
for i in range (size):
    for h in range(i+1):
        print ("+", end='')
    print ()

for i in range (size,0,-1):
    for h in range(i):
        print ("+", end='')
    print ()


for a in range(1,5):
    for b in range(1,5):
        print (b*a, end="\t")
    print ()

#Задание 3
x = int(input("Введите число: "))
for m in range (1,x+1):
    if m % 3 ==0:
        print ("Результат:", m)
print("_____________________________________________________________")

#Задание 4
numbers = [2,5,-15,4,6,-78,6,-3,11,-45]
sum = 0
count = 0
for num in numbers:
    if num > 0:
        sum += num
        count += 1
if count > 0:
    average = sum/count
else:
    average = 0
print ("Среднее значение всех положительных чисел в списке:", average)
print("_____________________________________________________________")

#Задание *
a = "*"
for i in range(1,10):
    print(" "*(10-i),a*i*2)