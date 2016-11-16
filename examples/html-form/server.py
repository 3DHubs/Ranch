import json
from flask import Flask, request, Response
from ranch import Address, AddressParts

PORT = 8000


def names_to_values(d):
    values = {}

    for part in AddressParts.__members__.values():
        if part.name in d:
            values[part] = d[part.name]

    return values


def store_new_values(address, new):
    parts = list(AddressParts.significant())
    parts += [AddressParts.postal_code, AddressParts.sorting_code]

    for part in parts:
        if part in new:
            if part in address.fields and \
               address.fields[part].value == new[part]:
                continue

            address.set_field(part, new[part])

    return address


def get_address_fields(a):
    ret = []
    for f in a.get_field_types():
        required = f['required']
        if f['key'] == AddressParts.name:
            required = True

        entry = {
            'key': f['key'].name,
            'label': f['label'],
            'required': required,
        }

        if f['options'] is not None:
            entry['options'] = f['options']
        ret.append(entry)
    return ret


app = Flask(__name__)


@app.route('/address', methods=['GET', 'POST'])
def address():
    a = Address()

    if request.method == 'GET':
        data = json.dumps(get_address_fields(a))

    elif request.method == 'POST':
        in_address = request.get_json()
        store_new_values(a, names_to_values(in_address))
        data = json.dumps(get_address_fields(a))

    return Response(data, mimetype='application/json')


@app.route('/')
def index():
    with open('index.html', 'r') as index_f:
        return index_f.read()


if __name__ == '__main__':
    app.run(debug=True)
