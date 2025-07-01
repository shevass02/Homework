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

#23/06/2025
    
# n1=int(input("enter - "))
# n2=int(input("enter - "))

# if n1>n2:
#     temp = n1
#     n1=n2
#     n2=temp
# i=n1
# while i<=n2:
#     print(i, end =" ")
#     i+=1

# money = (int(input("enter miney: ")))
# ice = (int(input("enter price: ")))

# number = 0
# while number < 300:
#     number += 1
#     if number % 3 != 0:
#         continue
#     elif number % 5 != 0:
#         print(number, "divides by 3")
#     elif number % 7 != 0:
#         print(number, "divides by 3 and 5")
#     else:
#         print(number, "divides by 3 and 5 and 7")

# start = 2
# end = 100

# for i in range(start, end+1):
#     k = 0
#     for j in range(i,1,-1):
#         if i%j==0:
#             k+=1
#     if k==1:
#        print(i, end=" ")

# size = int(input("Enter size - "))
# i = 0
# while i<size:
#     j = 0
#     while j<size:
#         if i==j:
#            print('1', end='')
#         else:
#            print('0', end='') 
#         j+=1
#     print()
#     i+=1


# for i in range(2,10):
#     for j in range(2,10):
#         print(f"{i}*{j}={i*j}")

#     print()        


# for c in range(5):
#     a = 2
#     b = 1
#     for f in range(5):
#         if c%2==0:
#             print(a, end='')
#             a+=2
#         else:
#             print(b, end='')
#             b+=2
#     print()


# for c in range(0,10):
#     a = 2
#     b = 1
#     for f in range(0,10):
#         if c%2==0:
#             print(a**2, end=' ')
#             a+=2
#         else:
#             print(-b**2, end=' ')
#             b+=2
#     print()


  


    


      
        
        
        
        
    




