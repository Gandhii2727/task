'''Задание 2. Найдите максимум и минимум в списке чисел.'''


# numbers = [-2, -3, 1, 4, 3, 8, 5, 10, 2, -1, 0, -2]


# min_num = max_num = numbers[0]


# for i in numbers:
#     if i > max_num:
#         max_num = i
#     if i < min_num:
#         min_num = i
    


# print(max_num, min_num)


'''Задание 3. Напишите программу, которая записывает в список все числа от 1 до 100, которые делятся на 7.'''

# numbers = []


# for number in range(1, 101):
#     if number % 7 == 0:
#         numbers.append(number)

        
# print(numbers)        



'''Задание 4. Напишите программу, которая записывает в новый список все элементы, которые больше 5.'''

# numbers = [1, 4, 3, 8, 5, 10, 2, -1, 0, -2]


# number1 = []


# for number in numbers:
#     if number > 5:
#         number1.append(number)

        
# print(number1)        






'''Напишите программу, которая меняет порядок элементов в списке на месте,
без использования встроенных функций (reverse(), reversed() и т.п.), можно записать в новий список.

[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
'''


number_list = [1, 2, 3, 4, 5]

number_reversed = []
# # range (3, 6, -1)
# # range (6, 2, -1)
# len_list = len(number_list)
# print(len_list)
# for elements in range(len_list - 1, -1, -1):
#     number_reversed.append(number_list[elements])


# print(number_reversed)    
for i in number_list:
    number_reversed.insert(0, i)

print(number_reversed)


