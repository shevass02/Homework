# У списку цілих, заповненому випадковими числами обчислити:

# Суму від'ємних чисел;
# Суму парних чисел;
# Суму непарних чисел;
# Добуток елементів з індексами кратними 3;
# Добуток елементів між мінімальним і максимальним елементом;
# Суму елементів, що знаходяться між першим і останнім додатними елементами.

# import random
# numbers = [random.randint(-50,50) for _ in range(10)]
# print("список:", numbers)
# i = 0
# sum_negative = 0
# sum_even = 0
# sum_odd = 0
# index_3 = 1

# while i<len(numbers):
#     if numbers[i]<0:
#         sum_negative+=numbers[i]
        
#     if numbers[i]%2 ==0:
#         sum_even+=numbers[i]
        
#     else:
#         sum_odd+=numbers[i]
        
#     if numbers[i]%3 ==0:
#         index_3*=numbers[i]
#     i+=1
# max_value = numbers[0]
# max_index = 0
# min_value = numbers[0]
# min_index = 0
# for i in range(1,len(numbers)):
#     if numbers[i]>max_value:
#         max_value = numbers[i]
#         max_index = i
#     if numbers[i]<min_value:
#         min_value = numbers[i]
#         min_index = i
# if min_index<max_index:
#         start = min_index+1
#         end = max_index
# else:
#         start = max_index+1
#         end = min_index
# prod = 1
# for i in range(start,end):
#     prod*=numbers[i]


        
# print("сума від'ємних: ",sum_negative)
# print("Сума парних: ",sum_even)
# print("сума непарних:", sum_odd)
# print("добуток елементів кратних 3: ", index_3)
# print("добуток між максимальним елементом і мінімальним: ",prod)

# Завдання 2
# Є список цілих, заповнений випадковими числами. На підставі даних цього масиву потрібно:

# Створити список цілих, що містить тільки парні числа з першого списку;
# Створити список цілих, що містить тільки непарні числа з першого списку;
# Створити список цілих, що містить тільки від'ємні числа з першого списку;
# Створити список цілих, що містить тільки додатні числа з першого списку.

# import random
# numbers = [random.randint(-50,50) for _ in range(5)]
# print("Список: ", numbers)

# even_numbers = []
# odd_numbers = []
# negative_numbers = []
# positive_numbers = []

# i = 0
# while i < len(numbers):  
#     num = numbers[i]
#     if num % 2 == 0:
#         even_numbers.append(num)
#     if num % 2 !=0:
#         odd_numbers.append(num)
#     if num < 0:
#         negative_numbers.append(num)
#     if num > 0:
#         positive_numbers.append(num)    
#     i += 1  

# print("Парні числа:", even_numbers)
# print("непарні числа:", odd_numbers)
# print("від'ємні числа:", negative_numbers)
# print("додатні числа:", positive_numbers)

# Завдання 3
# Користувач з клавіатури вводить список рядків. Необхідно знайти найкоротший рядок у списку. 
# Якщо таких рядків декілька, вивести перший.

# n = int(input("Введіть кількість рядків: "))
# lines = []
# for i in range(n):
#     line = input(f"Введіть рядок {i+1}: ")
#     lines.append(line)
# min_line = lines[0]
# min_lenght = len(min_line)
# for line in lines:
#     if len(line)<min_lenght:
#         min_line = line
#         min_lenght = len(line)
# print("Найкоротший рядок: ", min_line)

# Завдання 4
# Користувач з клавіатури вводить список рядків. Необхідно створити новий список,
# що містить рядки, які починаються із заданої літери. Результат вивести на екран.

# n = int(input("Введіть кількість рядків: "))
# symbol = input("Введіть символ: ")
# lines = []
# for i in range(n):
#     line = input(f"Введіть рядок {i+1}: ")
#     lines.append(line)
# filterred_lines  = []
# for line in lines:
#     if line.startswith(symbol):
#         filterred_lines.append(line)
# print(filterred_lines)



        






