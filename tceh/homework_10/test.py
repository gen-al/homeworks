# from flask import Flask

# app = Flask(__name__)

# @app.route('/hello/<user>/')
# def home(user):
#     return 'Hello, user: ' + user

# @app.route('/sum/<int:first>/<int:second>/')
# def summary(first, second):
#     return 'sum = {}'.format(first + second)

# @app.route('/conq/<text1>/<text2>/')
# def conq(text1, text2):
#     return text1 + text2

# @app.route('/')
# def welcome():
#     return 'Welcome!'

# if __name__ == '__main__':
#     app.run()

import json

def locales():
    loc = ['ru', 'en', 'it']
    return json.dumps(loc,sort_keys=True, indent=4)

print(locales())