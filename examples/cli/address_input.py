from ranch import Address, InvalidAddressException

a = Address()

while not a.is_valid():
    fields = a.get_field_types()

    last_field = fields[-1]

    if len(fields) > 1:
        for field in fields[:-1]:
            if field['key'] not in a.fields:
                last_field = field
                break

    try:
        a.set_field(last_field['key'], input(str(last_field['label']) + ': '))
    except InvalidAddressException as e:
        print('Error:', str(e))

print(a)
