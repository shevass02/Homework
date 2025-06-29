# Завдання 1
# Напишіть програму, яка запитує два цілих числа x і y, після чого обчислює і виводить 
# значення x у степені y.

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# power = 1
# for i in range(1, y+1):
#    power = power*x
# print(power)

# Завдання 2
# Користувач вводить ціле додатне число. Програма повинна знайти і вивести всі його дільники,
# а також їхню кількість.
# Приклад введення:
# Введіть число: 28.
# Приклад виведення:
# Дільники числа 28: 1, 2, 4, 7, 14, 28.
# Кількість дільників: 6.

# n=int(input("Enter number: "))
# divisor = 1
# for i in range(1,n+1):
#     if divisor%i==0:
# print(divisor)

import random
# import math

# for i in range(1,10):
    # print(random.randint(1,10))
    # print(random.random())

# print("Початок гри")  
# total=0
# wins=0
# losses=0 
# while True:
#     print("Зроби вибір") 
#     choice = int(input("камень - 1, Ножниці - 2, бумага - 3 -, гра закінчена - 0 - "))
#     if choice==1 or choice==2 or choice==3 or choice==0:
#         total+=1
#         pc_choice = random.randint(1,3)
#         print("Компьютер вибрав")
#         print("камень" if pc_choice==1 else ("ножниці"if pc_choice==2 else "бумага"))
#         if choice==pc_choice:
#             print("ничья")
#         elif (choice==1 and pc_choice==2) or (choice==2 and pc_choice==3) or (choice==3 and pc_choice==1):
#             print("вітаю, ви перемогли")
#             wins+=1

#         elif (choice==0):
#             print("гра закінчена")
#             break

#         else:
#             print("нажаль, ви програли")
#             losses+=1
#     else:
#         print("ти помилився з вибором")
# print(f"статистика по грі. Всього ігор{total}, перемог {wins}, поразок {losses}, ничья {total-losses-wins}")

#Програма загадує число від 1 до 100. Гравець повинен вгадати. Після кожної спроби
#програма каже більше або менше. Кількість спроб вивести у консоль
# print("початок гри ")
# import random
# los=0
# wins=0

# n2 = random.randint(1,100)

# while True:
#     n = int(input("Enter number - "))
    
#     if n>n2:
#         los+=1
#         print("меньше")
#     elif n<n2:
#         wins+=1
#         print("больше")
#     elif n==n2:
#         print(f"вы угадали. Всего попыток {los+wins+1}")
#         break



#Покупець вводить ціни товарів. Ціни вводяться доти, поки не введено 0. 
# Порахувати загальну суму покупки
# los=0
# while True:
#     n = float(input("Enter price - "))
#     print(n)
#     los=los+n
#     los+=1
#     if n==0:
#      print(los)
#      break

#Користувач вводить послідовно кількість голосів за трьох кандидатів. Обчисли хто виграв вибори
n1 = int(input("Enter the numbers of votes 1 - "))
n2 = int(input("Enter the numbers of votes 2 - "))
n3 = int(input("Enter the numbers of votes 3 - "))
if n1>n2 and n1>n3:
    print("виграв кандидат 1")
elif n2>n1 and n2>n3:
     print("виграв кандидат 2")
elif n3>n1 and n3>n2:
      print("виграв кандидат 3")
elif n1>n2 and n1==n3:
     print("кандидати 1 і 3 переходять у другий тур")
elif n2>n1 and n2==n3:
     print("кандидати 2 і 3 переходять у другий тур")
elif n2>n3 and n2==n1:
     print("кандидати 1 і 2 переходять у другий тур")

    
         
    
    





