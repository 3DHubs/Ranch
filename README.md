# Ranch

> _Ranch is a dressing… get it?_

Doing addressing is hard. There's too many [exceptions][falsehoods],
[differences][formats] and [human involvement][deliverability]; making the
entire process overwhelmingly [depressing][sadtopographies].

Luckily, we're not the first people to have faced this problem.
[Plenty][commerceguys] [of][i18n] [people][libpostal] have attempted to tackle
the problem of addressing, and plenty have succeeded! So no, Ranch isn't
reinventing the wheel entirely. Instead, we're working with Google's excellent
i18n dataset: downloading it, parsing it, outputting data.

Ranch is built as an object to store your address data in. So instead of having
you access a bunch of stuff and doing checks yourself, Ranch allows you to
enter address field data and poll for whatever the next set of fields is to
fill in.

After that you can simply call a `str(address)` to correctly format the address
for the address' locality. That's all you need to get a (technically)
deliverable postal address from your users.

[falsehoods]: https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/
[formats]: https://en.wikipedia.org/wiki/Address_(geography)#Mailing_address_format_by_country
[deliverability]: http://grcdi.blogspot.nl/2011/01/myth-of-deliverability.html
[sadtopographies]: https://www.instagram.com/sadtopographies/

[commerceguys]: https://github.com/commerceguys/addressing
[i18n]: https://github.com/googlei18n/libaddressinput
[libpostal]: https://github.com/openvenues/libpostal

## Setup

Ranch is currently built to run on Python 3.5, but it's not very complicated
and should work easily on other versions. We just don't test for that yet.
Setting up Ranch is as easy as running installing it through Pip:

```
pip install Ranch
```

Or check out the repository at the version you want, and install run

```
python setup.py install
```

## Usage

Documentation is written in the docstrings, but not yet automatically
generated. A very simple example of usage is like so:

```
from ranch import Address, AddressParts
a = Address()
a.set_field(AddressParts.country, 'NL')
a.set_field(AddressParts.name, 'John Doe')
a.set_field(AddressParts.organisation, '3D Hubs')
a.set_field(AddressParts.street_address, 'Frederiksplein 42')
a.set_field(AddressParts.postal_code, '1017 XN')
a.set_field(AddressParts.city, 'Amsterdam')

print(a)
# 3D Hubs
# John Doe
# Frederiksplein 42
# 1017 XN AMSTERDAM
# NETHERLANDS
```

Or, if you want to create dynamic forms, use `a.get_field_types()`, which will
return an array of FieldType objects, which have human-readable labels, valid
options, required values - all you need.

## Development

We strongly recommend running Ranch in a virtual environment. It should be
simple enough to get Ranch ready for development:

```
python -m venv ranch-env
pip install -r requirements.txt
```

That's all there is to it! If you need to update the address format export, run
the `scripts/ranch-download` script. It's automated to put it in the right
place, but you can always put it somewhere else if needed.

Building a new version includes a few things. First, increment the version
number in `setup.py` according to [SemVer][semver], then commit with a nice
description. Tag that commit with the release version (like `vX.Y.Z`). Then run
`python setup.py bdist_wheel` to build the package. That's all you need!

[semver]: http://semver.org/ "Semantic Versioning"
