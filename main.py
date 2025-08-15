import setup
from schedule.models import *


def add_subject():
    name = input("Назва предмета: ").strip()
    teacher_first = input("Ім'я вчителя: ").strip()
    teacher_last = input("Прізвище вчителя: ").strip()

    teacher = Teacher.objects.filter(first_name__iexact=teacher_first, last_name__iexact=teacher_last).first()
    if not teacher:
        print("Вчителя не знайдено")
        return

    if Subject.objects.filter(name__iexact=name, teacher=teacher).exists():
        print("Такий предмет у цього вчителя вже існує")
        return

    Subject.objects.create(name=name, teacher=teacher)
    print("Предмет додано")


def add_teacher():
    first_name = input("Ім'я вчителя: ").strip()
    last_name = input("Прізвище вчителя: ").strip()

    if Teacher.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name).exists():
        print("Такий вчитель вже існує")
        return

    Teacher.objects.create(first_name=first_name, last_name=last_name)
    print("Вчителя додано")


def add_class():
    name = input("Назва класу: ").strip()

    if Class.objects.filter(name__iexact=name).exists():
        print("Клас з такою назвою вже існує")
        return

    Class.objects.create(name=name)
    print("Клас додано")


def add_student():
    first_name = input("Ім'я учня: ").strip()
    last_name = input("Прізвище учня: ").strip()
    class_name = input("Назва класу: ").strip()

    school_class = Class.objects.filter(name__iexact=class_name).first()
    if not school_class:
        print("Клас не знайдено")
        return

    Student.objects.create(first_name=first_name, last_name=last_name, student_class=school_class)
    print("Учня додано")


def add_schedule():
    day = input("Дата (YYYY-MM-DD): ").strip()
    time = input("Час (HH:MM): ").strip()
    subject_name = input("Назва предмета: ").strip()
    class_name = input("Назва класу: ").strip()
    teacher_first = input("Ім'я вчителя: ").strip()
    teacher_last = input("Прізвище вчителя: ").strip()

    subject = Subject.objects.filter(name__iexact=subject_name).first()
    if not subject:
        print("Предмет не знайдено")
        return

    class_room = Class.objects.filter(name__iexact=class_name).first()
    if not class_room:
        print("Клас не знайдено")
        return

    teacher = Teacher.objects.filter(first_name__iexact=teacher_first, last_name__iexact=teacher_last).first()
    if not teacher:
        print("Вчителя не знайдено")
        return

    Schedule.objects.create(subject=subject, class_room=class_room, teacher=teacher, day=day, time=time)
    print("Заняття додано в розклад")


def add_grade():
    student_first = input("Ім'я учня: ").strip()
    student_last = input("Прізвище учня: ").strip()
    subject_name = input("Назва предмета: ").strip()
    grade_value = int(input("Оцінка (число): ").strip())
    date = input("Дата (YYYY-MM-DD): ").strip()

    student = Student.objects.filter(first_name__iexact=student_first, last_name__iexact=student_last).first()
    if not student:
        print("Учня не знайдено")
        return

    subject = Subject.objects.filter(name__iexact=subject_name).first()
    if not subject:
        print("Предмет не знайдено")
        return

    Grade.objects.create(student=student, subject=subject, grade=grade_value, date=date)
    print("Оцінку додано")


if __name__ == "__main__":
    while True:
        print("\n")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Додати заняття в розклад")
        print("6. Додати оцінку")
        print("7. Вихід")

        choice = input("Виберіть дію: ").strip()
        if choice == "1":
            add_subject()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            add_class()
        elif choice == "4":
            add_student()
        elif choice == "5":
            add_schedule()
        elif choice == "6":
            add_grade()
        elif choice == "7":
            break
        else:
            print("Невірний вибір")
