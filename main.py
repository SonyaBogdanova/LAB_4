"LAB_4"
def p1():
    try:
        chislo = int(input('Введите число: '))
        x = chislo % 3
    except ValueError:
        print ('Это не число!')
    else:
        if x == 0 and chislo !=0:
            print ('Число', chislo, 'делится на 3')
        elif chislo == 0:
            print ('Введён 0!')
        else:
            print ('Число', chislo, 'не делится на 3')

def p2():
    try:
        ch1 = int(input('Введите число: '))
        ch2 = 100 / ch1
    except ZeroDivisionError:
        print ('На ноль делить нельзя!')
    except ValueError:
        print ('Это не число!')
    else:
        print ('Результат деления 100 на введенное число: ', ch2)

def p3():
    date = input ('Введите дату в формате дд.мм.гггг: ')
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('Дата магическая!')
    else:
        print('Дата не является магической!')

def p4():
    ticket = input('Введите номер билета: ')
    x = 0
    y = 0
    if len(ticket) % 2 == 0:
        for i in ticket[0:int(len(ticket) / 2)]:
            x = x + int(i)
        for i in ticket[int(len(ticket) / 2): int(len(ticket)) +1]:
            y = y + int(i)
        if x == y:
            print('Билет счастливый!')
        else:
            print('Билет НЕсчастливый!')
    else:
        print('Количество цифр нечётно!')

p1(), p2(), p3(), p4()

