import math
while True:
    print('Выбирете действие:')
    print('1)Сложение  6)Корень числа')
    print('2)Вычитание 7)Факториал числа')
    print('3)Умножение 8)Синус числа')
    print('4)Деление   9)Косинус числа')
    print('5)Степень   10)Тангенс числа')
    func = int(input('Ваш выбор: '))
    if func >= 11:
        print('Вы выбрали неправильное действие')
        break
    elif func <= 0:
        print('Вы выбрали неправильное действие')
        break
    else:
        def go(func):
            match func:
                case 1:
                    x = float(input('Введите первое число: '))
                    y = float(input('Введите второе число: '))
                    print('Результат: ',x+y)
                case 2:
                    x = float(input('Введите первое число: '))
                    y = float(input('Введите второе число: '))
                    print('Результат: ',x-y)
                case 3:
                    x = float(input('Введите первое число: '))
                    y = float(input('Введите второе число: '))
                    print('Результат: ',x*y)
                case 4:
                    x = float(input('Введите делимое число: '))
                    y = float(input('Введите делитель число: '))
                    if y == 0:
                        print('НЕПРАВИЛЬНО! Делить на 0 запрещено')
                    print ('Результат: ',x/y)
                case 5:
                    x = float(input('Введите число: '))
                    y = float(input('Введите степень: '))
                    print ('Результат: ',x**y)
                case 6:
                    x = float(input('Введите число: '))
                    if x < 0:
                        print ('Вы ввели неправильное число')
                    else:
                        print ('Результат: ',(math.sqrt(x)))
                case 7:
                    x = int(input('Введите число: '))
                    if x < 0:
                        print('Вы ввели неправильное число')
                    else:
                        print ('Результат: ', (math.factorial(x)))
                case 8:
                    x = float(input('Введите число: '))
                    print ('Результат: ',(math.sin(x)))
                case 9:
                    x = float(input('Введите число: '))
                    print ('Результат: ',(math.cos(x)))
                case 10:
                    x = float(input('Введите число: '))
                    print ('Результат: ',(math.tan(x)))
    go(func)