from flask import Flask, request, Response
from ranch import Address, AddressParts, InvalidAddressException
from ranch.json import JSONEncoder
import os

ON_HEROKU = os.environ.get('ON_HEROKU')
if ON_HEROKU:
    PORT = int(os.environ.get('PORT'))
else:
    PORT = 3000

app = Flask(__name__)
json = JSONEncoder()

@app.route('/address', methods=['GET', 'POST'])
def address():
    a = Address()

    if request.method == 'GET':
        data = json.encode(a.get_field_types())

    elif request.method == 'POST':
        in_address = request.get_json()
        significant = list(AddressParts.significant())
        significant += [AddressParts.postal_code, AddressParts.sorting_code]

        sorted_fields = sorted(
            in_address.items(),
            key=lambda i: significant.index(AddressParts.from_string(i[0]))
        )
        for part, value in sorted_fields:
            try:
                a.set_field(part, value)
            except InvalidAddressException as e:
                return Response(
                    json.encode({'message': str(e)}),
                    mimetype='application/json',
                    status=400
                )

        data = json.encode(a.get_field_types())

    return Response(data, mimetype='application/json')

@app.route('/')
def index():
    return """<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <title>Ranch address form example</title>
</head>
<body>

<form class="js-form">
</form>

<p class="js-errors"></p>

<template id="js-text-field">
  <div>
    <label></label>:
    <input type="text" class="js-field">
  </div>
</template>

<template id="js-choices-field">
  <div>
    <label></label>:
    <select class="js-field">
      <option value="">Select…</select>
    </select>
  </div>
</template>


<script>
'use strict';

const form = document.querySelector('.js-form');
const textField = document.querySelector('#js-text-field');
const choicesField = document.querySelector('#js-choices-field');
const errors = document.querySelector('.js-errors');

function submitData() {
  let elements = Array.from(form.elements);
  if (event.target instanceof HTMLSelectElement) {
    elements.splice(elements.indexOf(event.target) + 1)
      .map(element => element.parentNode)
      .forEach(element => { element.parentNode.removeChild(element); });
  }

  const data = elements.reduce((obj, field) => {
    if (field.value !== '') {
      obj[field.dataset.key] = field.value;
    }
    return obj;
  }, {});

  window.fetch('/address', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: new Headers({ 'Content-Type': 'application/json' }),
  })
    .then(response => response.status < 400 ? response : Promise.reject(response))
    .then(parseFieldsResponse)
    .catch(response => {
      response.json()
        .then(error => {
          errors.innerText = error.message;
        });
    });
}

function createChoicesField(options) {
  const node = document.importNode(choicesField.content, true);
  const field = node.querySelector('.js-field');

  options.forEach(option => {
    field.add(new Option(option[0], option[1]))
  });

  return { node, field };
}

function parseFieldsResponse(response) {
  errors.innerText = '';

  response.json()
    .then(fields => {
      const changed = false;

      fields.forEach((fieldData, index) => {
        const formFields = Array.from(form.elements);
        const existingKeys = formFields.map(el => el.dataset.key);
        if (existingKeys.includes(fieldData.key)) {
          return;
        }

        let node, field;

        if (fieldData.options) {
          const options = Object.entries(fieldData.options)
            .sort((a, b) => {
              if(a[1] < b[1]) return -1;
              if(a[1] > b[1]) return 1;
              return 0;
            })
            .map(option => [option[1], option[0]]);

          ({ node, field } = createChoicesField(options));
        } else {
          node = document.importNode(textField.content, true);
          field = node.querySelector('.js-field');
        }

        node.querySelector('label').textContent = fieldData.label;
        field.dataset.key = fieldData.key;
        field.addEventListener('change', submitData);

        if (index > 0) {
          formFields[index - 1].after(node);
        } else {
          form.appendChild(node);
        }
      });
    });
}

window.fetch('/address')
  .then(parseFieldsResponse);
</script>
"""


if __name__ == '__main__':
    app.run(port=PORT)
