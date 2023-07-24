txt = (input('Введите текст: '))
if txt.isdecimal():
    b = bin(int(txt))
    o = oct(int(txt))
    h = hex(int(txt))
    print(b, o, h)
elif txt.isascii():
    print('текст написан в ASCII')
else:
    print('текст НЕ написан в ASCII')

# txt = input('Введите текст: ')
# print(txt, type(txt), id(txt))
# print(hash(txt))