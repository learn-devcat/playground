import random
import json

with open('cityStates.json') as c:
    locales = json.load(c)

for locale in locales['locations']:
    location: object = locale['city'] + ', ' + locale['state']

with open('streets.json') as s:
    streets = json.load(s)

for street in streets['street']:
    street_name: object = street['street']

for num in range (100):
    first = random.choice(first_name)
    last = random.choice(last_name)

    phone = f'{random.randint(100, 999)}-{random.randint(100,999)}-{random.randint(1000,9999)}'

    street_num = random.randint(100, 10000)
    name_street = random.choice(street_name)
    name_location = random.choice(location)
    zip_code = random.randint(10000, 99999)
    address = f'{street_nun} {name_street}\n{name_location} {zip_code}'

    email = first.lower() + '.' + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{email}\n\n{address}\n')
