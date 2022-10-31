__author__ = 'genal'

# Алгоритмы курса "Алгоритмы и структуры данных в Python"
# Часть 1


def turn_over(A:list):
    """
    Функция переворачивает массив задом наперед.
    Задачу сводим к поиску середины списка и
    поочередной замене симметричных от нее элементов
    """
    for i in range(len(A)//2):
        A[i], A[len(A) - 1 - i] = A[len(A) - 1 - i], A[i]


def shift_left(A:list):
    """
    Функция сдвигает массив на один элемент вправо.
    Помещаем первый элемент во временную переменную.
    Проходим все элементы списка со второго и присваиваем предыдущему
    элементу значение текущего.
    """
    tmp = A[0]
    for i in range(1, len(A)):
        A[i - 1] = A[i]
    A[-1] = tmp


def shift_right(A:list):
    """
    Функция сдвигает массив на один элемент вправо.
    Помещаем последний элемент во временную переменную.
    Проходя циклом от последнего элемента до второго включительно,
    присваиваем значение предыдущего элемента текущему.
    """
    tmp = A[-1]
    for i in range(len(A)-1, 0, -1):
        A[i] = A[i - 1]
    A[0] = tmp


def eratosfen(n:int):
    """
    Функция реализует решето Эратосфена - марктирует элементы чисел как
    простые или составные. Реализация - формирование массива True n-ой длины.
    Проходя по всем элементам маркируем четные текущим элементам значения
    элементы далее (вложенным циклом, куда включаем только четные текущему
    элементы).
    """
    A = [True] * n
    A[0] = A[1] = False

    for i in range(2, n):
        if A[i]:
            for k in range(i * 2, n, i):
                A[k] = False
    return A

# Печать списка:
# A = eratosfen(30)
# for i in range(len(A)):
#     print(i, ' - ', 'Простое' if A[i] else 'Составное')


def insert_sort(A:list):
    """
    Функция сотрирует список чисел методом вставки.
    Первый элемент массива принимается как уже отсортированный.
    Проходим массив поэлементно, добавляя элемент слева в виртульный
    массив, который обрабатываем справа налево - если два состедних
    элемента стоят не по порядку, меняем их местами
    """
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k] < A[k - 1]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -=1


def choise_sort(A:list):
    """
    Функция сотрируем массив методом выбора
    Проходим по каждому элементу массива с первого по предпоследний.
    Если текущий элемент больше сравниваемого - меняем их местами.
    """
    for i in range(0, len(A)-1):
        for k in range(i, len(A)):
            if A[k] < A[i]:
                A[i], A[k] = A[k], A[i]


def bubble_sort(A:list):
    """
    Функция сортирует массив методом пузырьковой сортировки.
    При каждом проходе в цикле последний элемент встанет на
    нужную позицию.
    Поочередно сравниваем два соседних элемента и меняем их местами,
    если правый элемент меньше левого.
    """
    for i in range(1, len(A)):
        for k in range(0, len(A) - i):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]



def count_sort(A:list, n:int):
    N = [0] * n
    for i in range(0, len(A)):
        N[A[i]] +=1
# Нужно дописать вставку отсортированных данных в итоговый массив


def factorial(n:int):
    """
    Функция для расчета факториала от числа, большего 1.
    Алгортим работает по принципу рекурсии.
    n! = (n - 1)! * n. Выражение n - 1 передается в вызываемую функцию.
    """
    assert n >= 1, 'Факториал не определен'
    if n == 1:
        return n
    return factorial(n-1)*n   


def gcd(a:int, b:int):
    """
    Функция реализует рекурсивный алгоритм Евклида по поиску
    наибольшего общего делителя.
    Если второе число не равно нулю, передаем следующей функции
    остаток от деления певого числа на второе, пока не получим остаток 0
    """
    return a if b == 0 else gcd(b, a % b)


def pow(a:float, n:int):
    """
    Функция возведения в степень через рекурсию
    """
    if n == 0:
        return 1
    else:
        return pow(a, n - 1) * a


def pow2(a:float, n:int):
    """
    Функция быстрого возведения в степень резе рекурсию
    и особый случай - когда степень - четная. В этом случае число можно
    сразу возвести в квадрат и вычислить его степень, сокращенную в два раза
    """
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow2(a, n - 1) * a
    else:
        return pow2(a ** 2, n // 2)


def moveTower(height,fromPole, toPole, withPole):
    """
    Алгоритм решения задачки "Ханойские башни".
    Алгоритм исходит из того, что мы уже заранее знаем, ка переместить
    n-1 кольца башни и указываем в решении, как переместить последнее кольцо:
    1. Переместить остальные кольца на временный стержень,
    2. Переместить последнее кольцо на целевой стержень,
    3. Переместить оставшиеся кольца на целевой стержень.
    """
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        print('moving disk', height, 'from',fromPole,'to',toPole)
        moveTower(height-1,withPole,toPole,fromPole)


def generate_number(n:int, m:int, prefix=None):
    """
    Функция генерирунт и печатает n-мерные числа из m знаков.

    """
    prefix = prefix or []
    if m == 0: # крайний случай рекурсии
        print(prefix)
        return
    for digit in range(n): # генерируем числа от 0 до n не включая
        prefix.append(digit)
        generate_number(n, m - 1, prefix)
        prefix.pop() # удаляем число для следующей итерации


def find(number:int, N:list):
    for i in range(len(N)):
        if number == N[i]:
            return True
    return False

def generate_permutation(n:int, m:int=-1, prefix=None):
    """
    Функция генерирунт и печатает n-мерные числа из m знаков.
    Функция проводит проверку на уникальность числа в последовательности
    """
    m = n if m == -1 else m
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for number in range(1, n + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(n, m - 1, prefix)
        prefix.pop()


def merge(A:list, B:list):
    """
    Функция проводит сортировку массива при слиянии двух
    предварительно отсортированных массивов.
    В итоговый массив попадает элемент, меньший из двух массивов при
    сравнении их поочередно между собой.
    """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            n += 1
            i += 1
        else:
            C[n] = B[k]
            n += 1
            k +=1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n +=1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n +=1
    return C

def merge_sort(A:list):
    """
    Функция сортирует массив через разделение массива на две части
    (примерно пополам) и слиянием через вызов внешней функции
    """
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0,middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]



def quick_sort(A:list):
    """
    Функция проводит быструю сортировку рекурсивным методом
    """
    if len(A) <= 1:
        return
    L = []; M = []; R = []
    barrier = A[0]
    for i in A:
        if i < barrier:
            L.append(i)
        elif i == barrier:
            M.append(i)
        else:
            R.append(i)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in (L + M + R):
        A[k] = x,
        k += 1


def check_sorted(A:list, ascending=True):
    """
    Функция определяет, отсортирован ли массив (с учетом направления
    сортировки)
    Для перехода между направлениями сортировки используется параметр
    ascending. Параметр в теле функции менят знак при операции сравнения
    """
    s = ascending * 2 -1
    flag = True
    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag


def left_bound(A:list, key):
    """
    Функция находит левую границу вхождения искомого элемента в отсортированном
    массиве.
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A:list, key):
    """
    Функция находит левую границу вхождения искомого элемента в отсортированном
    массиве.
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right




A = [2, 1, 6, 3, 7, 12, 89, 3, 2, 0, 11]
B = [1, 2, 3, 4, 5, 6, 7]
C = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(check_sorted(C, False))


