prices = [57.8, 46.51, 97, 12.34, 56.78, 9.10, 98.76, 54.32, 32.10, 68.48]
for price in prices:
    price = int ( round ( price * 100 ) )
    rubles = price // 100
    cents = price % 100
    print(f'{rubles:02d} руб {cents:02d} коп', end=', ')
print('')

prices.sort()
for price in prices:
    price = int(round(price * 100))
    rubles = price // 100
    cents = price % 100
    print(f'{rubles:02d} руб {cents:02d} коп', end=', ')
print('')

prices_desc = sorted(prices, reverse=True)
for price in prices_desc:
    price = int(round(price * 100))
    rubles = price // 100
    cents = price % 100
    print(f'{rubles:02d} руб {cents:02d} коп', end=', ')
print('')

for price in prices_desc[:5]:
    price = int(round(price * 100))
    rubles = price // 100
    cents = price % 100
    print(f'{rubles:02d} руб {cents:02d} коп', end=', ')
print('')

