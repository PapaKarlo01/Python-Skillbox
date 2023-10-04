def from10to2(a):
    s = ""
    while a > 0:
        s = str(a % 2) + s
        a = a // 2
    return s


def from10to8(a):
    s = ""
    while a > 0:
        s = str(a % 8) + s
        a = a // 8
    return s


def from10to16(a):
    s = ''
    h = '0123456789ABCDEF'
    while a > 0:
        s = h[a % 16] + s
        a = a // 16
    return s
      

a = input()
if a.find('.') == -1:
    if int(a) >= 1:
        a = int(a)
        first = from10to2(a)
        second = from10to8(a)
        third = from10to16(a)
        print(first + ', ' + second + ', ' + third)
    else:
        print("Неверный ввод")
else:
    print("Неверный ввод")
input()