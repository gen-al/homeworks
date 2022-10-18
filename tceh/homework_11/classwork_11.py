__author__ = 'Gen Andrey'

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import validators, IntegerField
import random

app = Flask('__main__')

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'This is secret key',
    WTF_CSRF_ENABLED = False,
)

class UserForm(FlaskForm):
    number = IntegerField(label='number', validators=[
        validators.NumberRange(min=1, max=10)
    ])


class Riddler(object):

    number = None

    def new_number(self):
        self.number= random.randint(1, 10)
        return self.number

# r = Riddler()
# quess_number = r.new_number


# +1. Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"
@app.route('/', methods = ['GET'])
def print_guess():
    r = Riddler()
    quess_number = r.new_number()
    return 'Число загадано.'
      
# +2. Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="
# +3. Если число угадано - загадываем новое число
@app.route('/guess', methods = ['GET', 'POST'])
def guess():
    while True:
        if request.method == 'POST':
            form = UserForm(request.form)
            if form.validate():
                if int(request.form['number']) == guess_number:
                    guess_number = r.new_number
                    return ('=', 200)
                elif int(request.form['number']) > guess_number:
                    return ('>', 200)
                else:
                    return ('<', 200)
            else:
                return 'Введено некорректное значение.', 400
        else:
            return 'По адресу следует направлять POST запросы.', 400


# +4. Flask при старте сервера - устанавливает seed для
# random, генерирует случайное число для угадывания

if __name__ == '__main__':
    app.run()
    random.seed(1)
    #print(quess_number)
    
    
    