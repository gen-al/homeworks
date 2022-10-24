from jinja2 import Template

__author__ = 'genal'


def print_template():
    t = Template('Hello {{something}}!')
    result = t.render(something='world')
    print(result)

def for_example(iterable=None):
    if iterable == None:
        iterable = range(1, 10)

    t = Template("""
        My favorite numbers are:
        {% for i in array %} {{i}} {% endfor %}
    """)

    result = t.render(array=iterable)
    print(result)

def if_example(value):
    t = Template("""
        {% if value <= 10 %}
        The value is lower or equal than 10
        {% else %}
        The value is greater than 10
        {% endif %}
    """)

    result = t.render(value=value)
    print(result)

if_example(5)