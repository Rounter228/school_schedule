import setup
from schedule.models import *


def menu():
    num = int(input("1. Додати предмет, 2. Додати вчителя 3. Додати клас 4. Додати учня 5. Додати розклад 6. Додати оцінку 0. Вийти"))
    return num


def subject_add():
    name = input("Введіть назву предмету: ")
    description = input("Введіть опис предмету: ")
    Subject.objects.create(name=name, description=description)


def teacher_add():
    first_name = input("Введіть ім'я вчителя: ")
    last_name = input("Введіть прізвище вчителя: ")
    id = int(input("Введіть ID предмету: "))
    while not id:
        sub = Subject.objects.get(id=id)
        if sub:
            Teacher.objects.create(first_name=first_name, last_name=last_name, subject = sub)
        else:
            print("ID не знайдено")
            id = int(input("Введіть ID предмету: "))



while True:
    num = menu()
    if num == 0:
        break
    elif num == 1:
        subject_add()
        print("Предмет додано")
    elif num == 2:
        teacher_add()
        print("Вчителя додано")
