# 1. Дано ціле число (int). Порахувати скільки нулів в цьому числі.

# number = 3760276601870170
# count = str(number).count('0')
# print(count)
####################################
# 2. Дано ціле число (int).
# Порахувати скільки нулів в кінці цього числа. Наприклад для числа 1002000 - три нулі

# number = 12300000
# go_loop = True
# count = 0
# while go_loop:
#     if number % 10 == 0:
#         count += 1
#         number /= 10
#     else:
#         go_loop = False
# print(count)

########################################

# 3. Дан список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший элемент з my_list
# стоїть на останньому месці в new_list. Якщо my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1, 3, 5, 587, "qwerty"]
# new_list = []
# first_value = my_list[0]
# last_value = my_list.pop()
# my_list = my_list[1::]
# new_list.append(last_value)
# new_list.append(my_list)
# new_list.append(first_value)
# print(new_list)

####################################

# 4. Дана строка в якій є числа (разділяються пробілами).
# Наприклад "43 більше за 34, але меньше за 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) в цій строкі.
# Для даного прикладу відповідь - 133. (використайте split и перевірку isdigit)

# my_str = "29 більше за 17, але менше за 46."
# symbol = my_str.split()
# my_list = []
# sum = 0
# for symbol in my_str:
#     if symbol.isdigit():
#         if my_str[my_str.index(symbol) + 1].isdigit():
#             sum += int(symbol) * 10
#         else:
#             sum += int(symbol)
# print(sum)

#######################
# 5. Дана строка my_str. Разділіть цю строку на пари з двох символів и поместіть ці пари в список.
# Якщо строка має непарну кількість символів, останній символ останньої пари має
# бути підкресленням ('_'). Приклади: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (використовуйте зрізи довжиною 2 символи)

# my_str = 'qwertyuiopa'
# new_list = []
# for pairs in my_str:
#     if my_str != '':
#          pairs = my_str[0:2]
#          if len(pairs) == 1:
#              pairs = pairs + "_"
#          new_list.append(pairs)
#          my_str = my_str[2::]
# print(new_list)

################################################

# 6. Дан список чисел. Порахуйте, скольки в цьому списку елементів,
# які більше за суму двох своїх сусідів (зліва и справа), и НАДРУКУЙТЕ КІЛЬКІСТЬ таких елементів.
# Крайні елементи списку не враховувати, оскільки в них недостньо сусідів.
# Для списка [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list = [3, 6, 2, 7, 4, 8, 9, 1, 5, 3]
# count = 0
# for number in my_list:
#     if number in range(0, len(my_list) - 1):
#         if number > int(my_list[my_list.index(number) - 1]) + int(my_list[my_list.index(number) + 1]):
#             count += 1
# print(count)


