import requests
r = requests.get('https://www.python.org')
r.status_code
print(r)

character = 'Python is a programming language that lets you work quickly'
if bytes(character, 'utf-8') in r.content:
    print(character)
else:
    print("NO")