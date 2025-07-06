# Завдання 1
# Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран 
# отриманий результат.

# text = input("enter text: ")
# symb = ['.','!','?']
# count = 0
# for char in text:
#     if char in symb:
#       count+=1
# print("Кількість речень в тексті:", count)



# Завдання 3
# Користувач вводить з клавіатури деякий текст. У програмі визначено набір зарезервованих слів. 
# Необхідно знайти в тексті всі зарезервовані слова і змінити їхній регістр на верхній. 
# Вивести на екран змінений текст.

# text = input("enter text: ")
# reserv = ['да', 'нет', 'семь', 'if', 'word']
# new_word = [
#     word.upper() if word.lower() in reserv 
#     else word for word in text.split()]
# print(" ".join(new_word))

# Завдання 4
# Користувач вводить рядок і два символи. Видаліть із рядка всі символи між першим 
# входженням першого символу і першим входженням другого символу, включаючи самі символи. 
# Виведіть результат.

# text = input("enter text: ")
# char1 = input("enter char 1: ")
# char2 = input("enter char 2: ")
# i1 = text.find(char1)
# i2 = text.find(char2)
# if i1!= -1 and i2!= -1 and i1<i2:
#     result = text[:i1] + text[i2+1:]
#     print("Результат: ")
#     print(result)
# else:
#     print(" символы не найдены ")

# Завдання 5
# Користувач вводить текст і набір символів. Видаліть з тексту всі слова, що містять 
# хоча б один з цих символів, і виведіть результат.

# text = input("enter text: ")
# char = input("Enter char: ")
# char_set = set(char)
# words = text.split()
# filt_word = [word for word in words 
#       if not any(c in char_set for c in word)       ]
# print(" ".join(filt_word))

# Завдання 6
# Створіть програму, яка із введеного тексту створює "зворотний текст" 
# (перевертає текст на рівні слів, а не символів). Наприклад, "я люблю Python" перетворюється 
# на "Python люблю я".

# text = input("enter text: ")
# words = text.split()
# res_words = words[: : -1]
# res_text = " ".join(res_words)
# print(res_text)



        