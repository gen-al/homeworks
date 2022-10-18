__author__ = 'Gen Andrey'

from contextlib import contextmanager
from msilib.schema import Error
import time

# +1. Дан класс:
class Lock(object):
    def __init__(self):
        self.lock = False

#     Сделать менеджер контекста, который может переопределить 
#     значение lock на True внутри блока контекста.

class Unlock(object):
    def __init__(self, obj):
        self.name = obj

    def __enter__(self):
        self.name.lock = True
        return self.name

    def __exit__(self, *args):
        self.name.lock = False

lock = Lock()
print(lock.lock)

with Unlock(lock) as l:
    print(lock.lock)

print(lock.lock)



# +2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные 
#    в теле и писал их в консоль, пример использования:
    
#     with no_exceptions():
#       1 / 0 # => logs: ZeroDivisionError

#     print('Done!') # => continues execution

@contextmanager
def no_exceptions():
    try:
        yield
    except Exception as e:
        print('logs: ' + str(e))
    finally:
        print('Done!')

with no_exceptions():
    1 / 0


# +3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, 
#    пример использования:
    
#     with TimeIt() as t:
#       some_long_function()

#     print('Execution time was:', t.time)

class TimeIt(object):
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, *args):
        print(f'Execution time was: {time.time() - self.start}')


with TimeIt():
    time.sleep(2)