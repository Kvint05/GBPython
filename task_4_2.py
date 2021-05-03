import requests

CURRENCIES = dict()
r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
if r.status_code == 200:
    for info_text in r.text.split('<Nominal>')[1:]:
        info = info_text.split("</Value>")[0].split('</Nominal><Name>')
        nominal = int(info[0])
        info2 = info[1].split('</Name><Value>')
        currency_type = info2[0]
        value = float(info2[1].replace(',', '.'))
        CURRENCIES[currency_type.lower()] = value / nominal


def currency_rates(currency):
    return round(CURRENCIES.get(currency.lower()), 2)


print(currency_rates('доллар США'))
print(currency_rates('Евро'))
