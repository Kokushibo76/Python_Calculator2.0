import math
while True:
    print('Выбирете действие')
    print('1)Сложение  6)Корень числа')
    print('2)Вычитание 7)Факториал числа')
    print('3)Умножение 8)Синус числа')
    print('4)Деление   9)Косинус числа')
    print('5)Степень   10)Тангенс числа')

    flag = True

    while flag == True:

        while True:
            try:
                func = int(input('Ваш выбор: '))
                break
            except ValueError:
                print("Неправильно, попробуйте снова")

        try:
            if func >= 1 and func <= 4:
                x = float(input('Введите первое число: '))
                y = float(input('Введите второе число: '))
                flag = False
            elif func == 5:
                x = float(input('Введите число: '))
                y = float(input('Введите степень: '))
                flag = False
            elif func == 6:
                x = float(input('Введите число: '))
                flag = False
            elif func == 7:
                x = int(input('Введите число: '))
                flag = False
            elif func >= 8 and func <= 10:
                x = float(input('Введите число: '))
                flag = False
            else:
                print("Попробуйте еще раз")
        except: print('error')

    try:
        match func:
            case 1:
                print("Результат: ", x + y)
            case 2:
                print("Результат: ", x - y)
            case 3:
                print("Результат: ", x * y)
            case 4:
                if y != 0:
                    print("Результат: ", x / y)
                else:
                    print("На ноль делить нельзя!")
            case 5:
                print("Результат: ", x**y)
            case 6:
                print("Корень из", math.sqrt(x))
            case 7:
                print ('Результат: ', math.factorial(x))
            case 8:
                print ('Результат: ',math.sin(x))
            case 9:
                print ('Результат: ',math.cos(x))
            case 10:
                print ('Результат: ',math.tan(x))
    except: print("error")