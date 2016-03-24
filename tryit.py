import json
from ranch import Address, InvalidAddressException


filename = input('Read data from: [data/export.json] ')
if filename == '':
    filename = 'data/export.json'

with open(filename, 'r') as data:
    specs = json.load(data)
    a = Address(specs)


while not a.is_valid():
    fields = a.get_field_types()

    last_field = fields[-1]

    if len(fields) > 1:
        for field in fields[:-1]:
            if field[0] not in a.fields:
                last_field = field
                break

    try:
        a.set_field(last_field[0], input(str(last_field[0]) + ': '))
    except InvalidAddressException as e:
        print('Error:', str(e))

print(a)
