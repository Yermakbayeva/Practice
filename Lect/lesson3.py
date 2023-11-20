#Задание 1 Приветствие пользователя

name = input("Введите ваше имя:")
print ("Здравствуйте,", name)

print("____________________________________________________________________")

#Задание 2+3 Рассчет средней оценки студента и сравнение оценок
bio = int (input("Введите ваш балл по биологии "))
geography = int (input("Введите ваш балл по георгафии "))
russian = int (input("Введите ваш балл по русскому "))
math = int (input("Введите ваш балл по математике "))
average = (bio+geography+russian+math)//4
print ("Ваша средняя успеваемость по предметам:", average)
print("===========================================================")
print ("Сравним ваши оценки и выведем лучший и худший результаты: ")
if bio > geography and bio > russian and bio > math:
       print("По биологии успеваемость лучше всего")
elif geography > bio and geography > math and geography > russian:
      print("По географии успеваемость лучше всего")
elif russian > bio and russian > geography and russian > math:
     print("По русскому успеваемость лучше всего")
else:
     print("По математике лучшая успеваемость")
if bio < geography and bio < russian and bio < math:
       print("По биологии худшая успеваемость")
elif geography < bio and geography < math and geography < russian:
      print("По географии худшая успеваемость")
elif russian < bio and russian < geography and russian < math:
     print("По русскому худшая успеваемость")
else:
     print("По математике худшая успеваемость")
print("____________________________________________________________________")
print("==================================================================")