# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

t = input('Введите 3  числа: ') 
if len(t) == 3: 
    l = int(t[0]) + int(t[1]) + int(t[2]) 
    print(l)
else:
    print('Вы ввели не 3-х значное число')  