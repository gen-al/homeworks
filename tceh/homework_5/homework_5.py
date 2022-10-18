# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
# Также у него должен быть следующий набор методов: know(person), который позволяет 
# добавить другого человека в список знакомых. И метод is_known(person),
# который возвращает знакомы ли два человека

class Person(object):
    def __init__(self, age=0, name='Noname'):
        self.age = age
        self.name = name
        self.known_persons = []

    def know(self, person):
        self.known_persons.append(person)

    def is_known(self, person):
        return person in self.known_persons


# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer(object):
    def __init__(self):
        self.values = []

    def log(self, *values):
        self.values = values
        print(self.values)


class FormattedPrinter(Printer):
    def fprint(self, *values):
        self.values = values
        print('***************************')
        self.log(values)
        print('***************************')



# *ЗАДАЧА 3:
# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека
# (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Human(object):
    def __init__(self, name):
        self.name = name

        self.dangerous = [
            'Lion',
            'Snake',
            'Wolf',
            ]

    def is_dangerous(self, animal):
        return animal.name in self.dangerous


class Animal(object):
    def __init__(self, name):
        self.name = name
