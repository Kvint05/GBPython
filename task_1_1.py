duration = int(input('Введите количество секунд: '))
d = duration // 86400
h = duration % 86400 // 3600
m = duration % 3600 // 60
s = duration % 60
if duration < 60:
    print(s, 'сек ')
elif 60 <= duration < 3600:
    print(m // 10, m % 10, ' мин ', s // 10, s % 10, ' сек ', sep='')
elif 3600 <= duration < 86400:
    print(h, ' час ', m // 10, m % 10, ' мин ', s // 10, s % 10, ' сек ', sep='')
else:
    print(d, ' дн ', h, ' час ', m // 10, m % 10, ' мин ', s // 10, s % 10, ' сек ', sep='')
