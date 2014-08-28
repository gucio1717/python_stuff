from jinja2 import Template

rps = [{'n': 1, 'n': 2, 'n': 3}]

template = Template('''
{% for i in rps %}
{{ i }}
{% endfor %}
''')

template.render(rps=rps)
