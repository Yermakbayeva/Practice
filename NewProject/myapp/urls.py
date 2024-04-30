list_1 = {
    1:
        {
        "name":"Ипотека",
        "sum": 70000,
        "stat": 'Оплачено'
        },
    
    2:
        {"name":"Тариф",
        "sum": 2500,
        "stat": "Оплачено"
        },
    
    3:
        {"name":"Коммунальные услуги",
        "sum": 10546,
        "stat": "Не оплачено"}
    }


def viv(list_1):
    for k,v in list_1.items():
        print("Номер в списке: ", k)
        print("Наименование расходов: ",v ["name"])
        print("Сумма затрат: ",v["sum"])
        print("Статус выполнения: ",v["stat"])

def add(list_1):
    new = int(input("Введите нумерацию: "))
    name1 = input("Введите наименование расходов: ")
    sum1 = int(input("Введите сумму: "))
    stat1 = input ("Введите статус выполнения: ")
    list_1[new] = {"name":name1,"sum": sum1,"stat":stat1} #Функция на добавление новых расходов в список

def clear(list_1):
    del_name = int(input("Введите номер в списке расходов, который нужно удалить: "))
    if del_name in list_1:
        del list_1[del_name]
    for k,v in list_1.items():
        print("Номер: ", k)
        print("Наименование расходов: ",v ["name"])
        print("Сумма: ",v["sum"])
        print("Статус выполнения: ",v["stat"])
    else:
        print('Задача не найдена')#Функция удаления выбранных расходов

def search (list_1):
    num = input("Введите номер в списке расходов ")
    if num in list_1:
        print (f"Вот ваша запись {num}: {list_1[num]}")
    else:
        print ("Извините, данный номер не найден")#Функция поиска    

def update(list_1):
    number = int(input("Введите номер в списке в который хотели бы внести изменения: "))
    name2 = input("Введите новое наименование расходов: ")
    sum2 = int(input("Введите новую сумму: "))
    stat2 = input("Введите новый статус: ")
    list_1[number] = {"name":name2,"sum": sum2,"stat":stat2} #Функция на изменения имеющегося списка расходов