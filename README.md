# Ranch

> _Ranch is a dressing… get it?_

## In which addressing is easy
Doing addressing is hard. There's too many [exceptions][falsehoods],
[differences][formats] and [human involvement][deliverability]; making the
entire process overwhelmingly [depressing][sadtopographies].

## In which addressing has never been done before
Luckily, we're not the first people to have faced this problem.
[Plenty][commerceguys] [of][i18n] [people][libpostal] have attempted to tackle
the problem of addressing, and plenty have succeeded! So no, ranch isn't
reinventing the wheel entirely. Instead, we're working with Google's excellent
i18n dataset: downloading it, parsing it, outputting data.

## In which I have to do everything myself
Ranch is built as an object to store your address data in. So instead of having
you access a bunch of stuff and doing checks yourself, ranch allows you to
enter address field data and poll for whatever the next set of fields is to
fill in.

After that you can simply call a `str(address)` to correctly format the address
for the address' locality. That's all you need to get a (technically)
deliverable postal address from your users.

## In which all that made sense
See `try_me.py` for an example: a commandline-based address form.

[falsehoods]: https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/
[formats]: https://en.wikipedia.org/wiki/Address_(geography)#Mailing_address_format_by_country
[deliverability]: http://grcdi.blogspot.nl/2011/01/myth-of-deliverability.html
[sadtopographies]: https://www.instagram.com/sadtopographies/

[commerceguys]: https://github.com/commerceguys/addressing
[i18n]: https://github.com/googlei18n/libaddressinput
[libpostal]: https://github.com/openvenues/libpostal
