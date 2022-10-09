# Задача: реализовать игру в загадки
# Требования:
# Программа выводить в консоль текст загадки и ждать ввода пользователя
# Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
# Загадок должно быть 10, тематика вопросов должна быть по первому занятию
# Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
# Программа должна в конце игры сказать, сколько ответов дал пользователь: сколько из них было верных
# Программа должна не учитывать регистр ответа: "Python" и "python" оба должны быть правильным ответом на вопрос "Какой язык мы учим?"

questions = {
    'Какой язык вы изучаете?': 'Python',
    'Кто автор языка Python?':'Гвидо ван Россум',
    'Что обозначет конструкция if?':'Условие',
    'Неизменяемый массив в Python.':'tuple',
    'На какой язык похож синтаксис Python?':'Английский',
    'Как называется этот курс?':'tceh'}

answers = 0
total = 0

for key,value in questions.items():
    if input(key + '>>> ').upper() == value.upper():
        print('Верно!')
        answers += 1
    else:
        print('Ошибка!')
    total += 1

print('Всего задано вопросов: {}'.format(total))
print('Правильных ответов: {}'.format(answers))


# Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон

a = int(input('Введите целое значение одной стороны прямоугольника >>> '))
b = int(input('Введите целое значение второй стороны прямоугольника >>> '))

print('Площадь прямоугольника равна {}'.format(a * b))

# Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-". В зависимости от знака выводит их сумму или разницу

a = int(input('Введите первое целое число >>> '))
b = int(input('Введите второе целое число >>> '))
sign = input('Введите знак "+" или "-" для определния действия >>> ')

if sign == '+':
    print('Сумма двух чисел = {}'.format(a + b))
elif sign == '-':
    print('Разность чисел = {}'.format(a - b))
else:
    print('Введен некорректный знак!')


# Напишите программу, которая находит все простые числа между 0 и пользовательским числом

list_numbers = list()
digit = int(input('Введите целое положительное число >>> '))

for x in range(2, digit + 1):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        list_numbers.append(x)

print(list_numbers)


# Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами

number_1 = int(input('Введите первое число >>> '))
number_2 = int(input('Введите второе число >>> '))
numbers = list()

for i in range(number_1, number_2):
    if i % 5 == 0:
        numbers.append(i)

print(numbers)