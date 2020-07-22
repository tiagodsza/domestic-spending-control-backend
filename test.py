import re

email = 'tiagogmail.com.br'

valid = re.search(r'\w{2,50}@\w{2,15}\.[a-z]{2,3}\.?([a-z]{2,3})?', email)

if valid:
    print('Email correto')
else:
    print('Email incorreto')