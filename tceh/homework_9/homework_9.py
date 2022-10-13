import requests
import json
import re

# + Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.

import sys

def read_file_data(filename):
    with open(filename) as f:
        return f.read()

def write_to_file(filename, content, mode = 'w'):
    with open(filename, mode = mode) as f:
        f.write(content)


# + Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск


def write_headres_request(site, filename):
    request_object = requests.get(site)
    json_data = json.dumps(dict(request_object.headers), sort_keys=True, indent=4)

    with open(filename, mode = 'w') as f:
        f.write(json_data)

# write_headres_request('https://jsonplaceholder.typicode.com/comments', 'headers.json')


# + Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
# Ответить себе на вопрос удобно ли так делать?

def print_links(url):
    url_content = str(requests.get(url).content)
    pattern_group = r'<a[^><]*href=[\'"]([^><\'"]*)[\'"][^><]*>'
    name = re.findall(pattern_group, url_content)
    print(name)

# print_links('https://habrahabr.ru/')