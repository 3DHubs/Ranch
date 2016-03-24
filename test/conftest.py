import json
import pytest
import ranch as addressing


@pytest.fixture
def ranch():
    return addressing


@pytest.fixture
def AddressParts():
    return addressing.AddressParts


@pytest.fixture
def address():
    with open('test/data.json', 'r') as js:
        data = json.load(js)
    return addressing.Address(data)


@pytest.fixture
def address_china(AddressParts, address):
    address.set_field(AddressParts.country, 'CN')
    address.set_field(AddressParts.admin_area, '宁夏回族自治区')
    address.set_field(AddressParts.city, '银川市')
    address.set_field(AddressParts.dependent_locality, '兴庆区')

    return address


@pytest.fixture
def address_canada(AddressParts, address):
    address.set_field(AddressParts.country, 'CA')
    address.set_field(AddressParts.admin_area, 'NT')
    address.set_field(AddressParts.city, 'Someplace')

    address.set_field(AddressParts.name, 'Bar foo')
    address.set_field(AddressParts.street_address, '15 Foo bar')
    address.set_field(AddressParts.postal_code, 'X0E 2Y7')
    return address
