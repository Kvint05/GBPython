import requests
from decimal import Decimal
import datetime


def get_parc(resp, argv, text):

    return resp.text.split(argv)[1].split(text)[1][1:-2]


def currency_rates(arg):

    arg = arg.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    if response.text.find(arg) != -1:
        nominal = int(get_parc(response, arg, "Nominal"))
        my_date = datetime.datetime.strptime(response.text.split("Date")[1].split('"')[1], "%d.%m.%Y").date()
        name = get_parc(response, arg, "Name")

        new_value = Decimal(".".join(get_parc(response, arg, "Value").split(','))).quantize(Decimal("1.00"))

        return [my_date, name, new_value / nominal]


if __name__ == '__main__':
    lst = currency_rates("доллар США")
    print(f"на  {lst[0]} Курс 1 {lst[1]} равен {lst[2]} рублей")
    lst = currency_rates("Евро")
    print(f"на  {lst[0]} Курс 1 {lst[1]} равен {lst[2]} рублей")

# в общем, творческая переработка не получилась((