
print("Введите выражение в формате \"число1 операция число2\" 2. Для прекращения работы напишите stop или стоп")
lst_pls = []
lst_mns = []
lst_mltp = []
lst_dvs = []

while 1 :

        expr_a = 0
        expr_b = 0
        expr_res = 0

        expr = input()
        expr_splt = list(expr.split(" "))
        if expr == "stop" or expr == "стоп":
            print("Работа Калькулятора завершена")
            break
        i = 1


        for dgt in reversed(expr_splt[0]):
            expr_a += int(dgt) * 10 * i
            i += 1
        expr_a /= 10

        i = 1
        for dgt in reversed(expr_splt[2]):
            expr_b += int(dgt) * 10 * i
            i += 1
        expr_b /= 10

        if ord(expr_splt[1]) == 43:
             expr_res = expr_a + expr_b
             lst_pls.append(str(expr) + " = " + str(expr_res))
             print(expr_res)
        elif ord(expr_splt[1]) == 45:
            expr_res = expr_a - expr_b
            lst_mns.append(str(expr) + " = " + str(expr_res))
            print(expr_res)
        elif ord(expr_splt[1]) == 42:
            expr_res = expr_a * expr_b
            lst_mltp.append(str(expr) + " = " + str(expr_res))
            print(expr_res)
        elif ord(expr_splt[1]) == 47:
            expr_res = expr_a / expr_b
            lst_dvs.append(str(expr) + " = " + str(expr_res))
            print(expr_res)
        elif ord(expr_splt[1]) > 47 or ord(expr_splt[1]) < 43 or ord(expr_splt[1]) == 46:
            print("ОШИБКА")
            break


        print("+ :" , lst_pls)
        print("- :" , lst_mns)
        print("* :" , lst_mltp)
        print("/ :" , lst_dvs)



