import re


def email_parse(email_address):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email_address)
    if not result:
        raise ValueError(f'Электронный адрес невалиден: {email_address}')
    return result.groupdict()


print(email_parse('relax03@mail.ru'))
print(email_parse('kvint05@mail.ru'))
