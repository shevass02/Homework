# Завдання 2
# Користувач вводить з клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити 
# на екрані вертикальну лінію 
# із введеного символу, зазначеної довжини.

# line = int(input("Enter lenght of the line - "))
# symbol = input("Enter symbol - ")
# i = 1
# while i<=line:
#     i+=1
#     print(symbol)



# Завдання 1
# Користувач вводить із клавіатури два числа. Потрібно порахувати окремо суму парних, 
# непарних і чисел, кратних 9 у вказаному діапазоні, а також середньоарифметичне кожної групи.

# num1 = int(input("Enter the first number  - "))
# num2 = int(input("Enter the second number - "))
# even_sum = 0
# even_count = 0
# odd_sum = 0
# odd_count = 0
# mult_sum = 0
# mult_cont = 0
# low = min(num1,num2)
# slow = max(num1,num2)
# for i in range(low,slow+1):
#     if i%2==0:
#         even_sum+=i
#         even_count+=1
#     else:
#         odd_sum+=i
#         odd_count+=1
#     if i%9==0:
#         mult_sum+=i
#         mult_cont+=1
# even_aver = even_sum/even_count if even_count>0 else 0        
# odd_aver = odd_sum/odd_count if odd_count>0 else 0        
# mult_aver = mult_sum/mult_cont if mult_cont>0 else 0        
# print(f"сума парних чисел:{even_sum}, Середнє арифметичне:{even_aver}")
# print(f"сума непарних чисел:{odd_sum}, Середнє арифметичне:{odd_aver}")
# print(f"сума чисел кратних 9:{mult_sum}, Середнє арифметичне:{mult_aver}")

 


# Завдання 3
# Користувач вводить із клавіатури числа. Якщо число більше нуля потрібно вивести
# напис "Number is positive", якщо менше нуля "Number is negative", якщо дорівнює
# нулю "Number is equal to zero". Коли користувач вводить число 7 програма припиняє 
# свою роботу і виводить на екран напис "Good bye!".

# while True:
#   num = int(input("Enter number - "))
#   if num==7:
#      print("Good bye!")
#      break
#   elif num>0:
#    print("Number is positive")
#   elif num<0:
#    print("Number is negative")
#   else:
#    print("Number is equal to zero")

# Завдання 4
# Користувач вводить із клавіатури числа. Програма повинна підраховувати суму, 
# максимум і мінімум, введених чисел. Коли користувач вводить число 7 програма припиняє 
# свою роботу і виводить на екран напис "Good bye!".

# while True:
#  num1 = int(input("Enter the first number  - "))
#  num2 = int(input("Enter the second number - "))
#  sum = 0
#  if num1==7 or num2==7:
#     print("Good bye!")
#     break
#  sum=num1+num2
#  print("sum - ",sum)
#  if num1>num2:
#    print("max - ",num1)
#    print("min - ",num2)
#  elif num1<num2:
#    print("max - ",num2)
#    print("min - ",num1)
    





