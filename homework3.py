from random import randint

# Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 10.
# Користувач намагається вгадати число. Програма може давати підказки тільки "More", "Less", "You won!"
#######################################################################

# rand_value = randint(1, 10)
#
# go_loop = True
# while go_loop:
#     value = input('Guess the number from 1 to 10: ')
#     try:
#         value_int = int(value)
#         if value_int < rand_value:
#             print('More')
#         elif value_int > rand_value:
#             print('Less')
#         elif value_int == rand_value:
#             print('You won!')
#             go_loop = False
#
#     except ValueError:
#         print('ValueError, try again')

#####################################################################
# Написати програму в якій випадковим чином створюється число в діапазоні від 1 до 12.
# Програма виводить на екран число, яке створено і назву місяця, який відповідає цьому числу.

# rand_value = randint(1, 12)
# if rand_value == 1:
#     print('1 - January')
# elif rand_value == 2:
#     print('2 - February')
# elif rand_value == 3:
#     print('3 - March')
# elif rand_value == 4:
#     print('4 - April')
# elif rand_value == 5:
#     print('5 - May')
# elif rand_value == 6:
#     print('6 - June')
# elif rand_value == 7:
#     print('7 - July')
# elif rand_value == 8:
#     print('8 - August')
# elif rand_value == 9:
#     print('9 - September')
# elif rand_value == 10:
#     print('10 - October')
# elif rand_value == 11:
#     print('11 - November')
# elif rand_value == 12:
#     print('12 - December')
#####################################################################
#Написати програму в якій користувач вводить два цілих числа.
# Програма виводить результат піднесення першого числа у степінь відповідний другому числу.
# Зробити обробку всіх можливих помилок.
# В разі неможливості виконання дії - вивести відповідне повідомлення. ("Введено не число", тощо ... )
#######################################################################
# go_loop = True
# while go_loop:
#     value_1 = input('Введіть перше ціле число: ')
#     value_2 = input('Введіть друге ціле число: ')
#     try:
#         value_int_1 = int(value_1)
#         value_int_2 = int(value_2)
#         value_int = value_int_1 ** value_int_2
#         print(value_int)
#         go_loop = False
#     except ValueError:
#         print('Введено не число або невірний формат числа, спробуйте знову')
