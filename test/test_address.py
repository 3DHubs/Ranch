import pytest


def test_address_initialises(address):
    assert(address.specs != {})


def test_set_fields(AddressParts, address):
    address.set_field(AddressParts.country, 'CA')
    address.set_field(AddressParts.admin_area, 'AB')
    assert address.get_specs()["zip"] == 'T'


def test_get_field_types(AddressParts, address):
    address.set_field(AddressParts.country, 'CA')

    fields = address.get_field_types()
    assert len(fields) == 2

    field_types = [field['key'] for field in fields]
    assert AddressParts.country in field_types
    assert AddressParts.admin_area in field_types

    assert len(fields[field_types.index(AddressParts.country)]['options']) == 4

    admin_area = fields[field_types.index(AddressParts.admin_area)]
    assert len(admin_area['options']) == 26


def test_field_types_no_more_options(AddressParts, address):
    address.set_field(AddressParts.country, 'CA')
    address.set_field(AddressParts.admin_area, 'NT')

    field_types = [field['key'] for field in address.get_field_types()]

    assert AddressParts.city in field_types
    assert AddressParts.street_address in field_types
    assert AddressParts.organisation in field_types
    assert AddressParts.name in field_types
    assert AddressParts.postal_code in field_types

    assert AddressParts.dependent_locality not in field_types


def test_field_types_take_backsies(AddressParts, address):
    address.set_field(AddressParts.country, 'CA')
    address.set_field(AddressParts.admin_area, 'NT')

    address.set_field(AddressParts.country, 'CN')

    field_types = [field['key'] for field in address.get_field_types()]
    assert AddressParts.city not in field_types


def test_field_types_order(AddressParts, address):
    address.set_field(AddressParts.country, 'CA')
    address.set_field(AddressParts.admin_area, 'NT')

    field_types = [field['key'] for field in address.get_field_types()]
    assert field_types == [
        AddressParts.country,
        AddressParts.admin_area,

        AddressParts.name,
        AddressParts.organisation,
        AddressParts.street_address,
        AddressParts.city,
        AddressParts.postal_code,
    ]


def test_set_city(AddressParts, address_china):
    assert address_china.get_specs()["zipex"] == '750001'


def test_postal_code(ranch, AddressParts, address):
    address.set_field(AddressParts.country, 'CA')
    address.set_field(AddressParts.admin_area, 'NT')
    address.set_field(AddressParts.postal_code, 'X0E 2Y7')


def test_invalid_postal_code(ranch, AddressParts, address_canada):
    address = address_canada

    with pytest.raises(ranch.InvalidAddressException) as excinfo:
        address.set_field(AddressParts.postal_code, 'H3Z 2Y7')

    assert str(excinfo.value) == 'Invalid postal code'


def test_stringify(address_canada):
    address = address_canada

    assert str(address) == "\n".join((
        'BAR FOO',
        '15 FOO BAR',
        'SOMEPLACE NT X0E 2Y7',
        'CANADA',
    ))
