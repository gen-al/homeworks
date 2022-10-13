from flask import Flask, request, jsonify
from wtforms import StringField, validators
from flask_wtf import FlaskForm
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


class UserForm(FlaskForm):
    email = StringField(label='e-mail', validators=[
        validators.Email(),
        validators.InputRequired()
    ])
    password = StringField(label='password', validators=[
        validators.Length(min=6),
        validators.EqualTo('confirm_password')
    ])
    confirm_password = StringField(label='confirm_password', validators=[
        validators.Length(min=6)
    ])

# Реализовать на Flask
# 1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']

@app.route('/locales')
def locales():
    return jsonify(['ru','en', 'it'])


# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму

@app.route('/sum/<int:first>/<int:second>/')
def summary(first, second):
    return 'sum = {}'.format(first + second)


# 3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'

@app.route('/greet/<name>')
def welcome(name):
    return 'Hello, {}'.format(name)


# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают.
# Возрващать пользователю json вида: 
#  "status" - 0 или 1 (если ошибка валидации),
#  "errors" - список ошибок, если они есть,
#  или пустой список.

@app.route('/form/user', methods=['GET', 'POST'])
def form_user():

    status_code = {
        'valid': 0,
        'invalid': 1,
    }

    if request.method == 'POST':
        form = UserForm(request.form)
        if form.validate():
            return jsonify(status_code['valid'])
        else:
            return jsonify(status_code['invalid']), form.errors
    if request.method == 'GET':
        return ('This page for POST method.', 200)


# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404.

@app.route('/serve/<filename>')
def read_file(filename):
    if os.path.exists('C:\\Users\\andre\\Documents\\Projects\\homeworks\\tceh\\homework_10\\files\\' + filename):
        with open('C:\\Users\\andre\\Documents\\Projects\\homeworks\\tceh\\homework_10\\files\\' + filename) as f:
            return f.read()
    else:
        return ('File not exists.', 404)


if __name__ == '__main__':
    app.run()