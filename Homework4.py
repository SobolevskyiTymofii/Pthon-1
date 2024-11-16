# 1) У вас є список my_list із значеннями типу int.
# Роздрукувати значення, які більше 100.
# Завдання виконати за допомогою циклу for.
#############################################
# my_list = [1, 78, 6, 184, 985, 2786, 829, 107899, 5978, 386, 107, 78, 83078]
# for item in my_list:
#     if item > 100:
#         if item < 1000:
#                 print(item)
####################################################
# 2) У вас є список my_list зі значеннями типу int і порожній список my_results.
# Додати my_results ті значення, які більше 100.
# Роздрукувати список my_results.
# Завдання виконати за допомогою циклу for.

# my_list = [1, 78, 6, 184, 985, 2786, 829, 107899, 5978, 386, 107, 78, 83078]
# my_results = []
# for item in my_list:
#     if item > 100:
#         if item < 1000:
#                 my_results.append(item)
# print(my_results)

####################################

# 3) У вас є список my_list із значеннями типу str. Створити новий список до якого помістити
# елементи з my_list за таким правилом:
# Якщо строка стоїть на непарному місці my_list, то її замінити на обернену строку (Наприклад "qwe" на "ewq")
# Якщо на парному – залишити без зміни.
# Завдання зробити за допомогою циклу for та функції enumerate.

# my_list = ["qwe", "rty", "uio", "pas", "dfg"]
# new_list = []
# for count, item in enumerate(my_list):
#     if count % 2 == 1:
#         new_list.append(item[::-1])
#     else:
#         new_list.append(item)
# print(new_list)

# 4) У вас є рядок my_string = '0123456789'.
# Згенерувати цілі числа (тип int) від 0 до 99 і помістити в список.
# my_string1 = "0123456789"
# my_string2 = "0123456789"
# my_list = []
# for symb_1 in my_string1:
#     for symb_2 in my_string2:
#         if symb_1 == "0":
#             symb_12 = int(symb_2)
#             my_list.append(symb_12)
#         else:
#             symb_12 = symb_1 + symb_2
#             symb_12 = int(symb_12)
#             my_list.append(symb_12)
#
# print(my_list)





