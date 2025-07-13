# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку 
# парних і непарних чисел. Результати вивести на екран.

# numbers = list(map(int, input("Enter numbers: ").split()))
# even_count = 0
# odd_count = 0
# i = 0
# while i < len(numbers):
#     if numbers[i]%2 == 0:
#         even_count+=1
#     else:
#         odd_count+=1
#     i+=1
# print("парні числа: ",even_count)
# print("непарні числа: ",odd_count)

# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне 
# і мінімальне значення у списку. Результати вивести на екран.

# numbers = list(map(int, input("Enter numbers: ").split()))
# min_value = numbers[0]
# max_value = numbers[0]
# for num in numbers:
#     if num< min_value:
#         min_value = num
#     if num>max_value:
#         max_value = num
# print("Максимальне число: ", max_value)
# print("мінімальне число: ", min_value)

# Завдання 3
# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний 
# елемент і максимальний, від'ємний елемент, порахувати кількість від'ємних елементів, 
# порахувати кількість додатних елементів, порахувати кількість нулів. Результати вивести на екран.

# import random
# numbers = [random.randint (-50,50) for _ in range(10) ]
# print("список цілих чисел: ",numbers)
# min_positive = None
# max_negative = None
# count_negative = 0
# count_positive = 0
# count_zero = 0
# i = 0
# while i<len(numbers):
#     num = numbers[i]
#     if num>0:
#         count_positive+=1
#         if min_positive is None or num<min_positive:
#             min_positive = num
#     elif num<0:
#         count_negative+=1
#         if max_negative is None or num>max_negative:
#             max_negative = num
#     else:
#         count_zero+=1
#     i+=1
# print("мінімальний додатній елемент: ",min_positive)
# print("максимальний від'ємний елемент: ",max_negative)
# print("кількість від'ємних елементів: ", count_negative)
# print("кількість додатніх елементів: ", count_positive)
# print("кількість нулів: ", count_zero)

# Завдання 4
# Користувач із клавіатури вводить список цілих чисел і деяке число. 
# Необхідно видалити зі списку всі елементи, які менші за задане число. 
# Результат вивести на екран.

# numbers = list(map(int, input("Enter numbers: ").split()))
# number = int(input("Enter number: "))
# i = 0
# while i < len(numbers):
#     if numbers[i] < number:
#         numbers.pop(i)
#     else:
#         i+=1
# print("список після видалення:", numbers)



