# Завдання 1
# Користувач вводить з клавіатури рядок. Порахуйте кількість букв, цифр у рядку. 
# Виведіть обидві кількості на екран.

# mes = input("Введіть рядок - ")
# let = 0
# dig = 0
# for char in mes:
#     if char.isalpha():
#         let+=1
#     elif char.isdigit():
#         dig+=1
# print("Кількість букв - ", let)
# print("Кількість цифр - ", dig)

# Завдання 2
# Користувач вводить з клавіатури рядок і символ для пошуку. Порахуйте скільки разів у рядку 
# зустрічається шуканий символ. Отримане число виведіть на екран.

# text = input("Enter text - ")
# symb = input("Enter symbol - ")
# count = 0
# for char in text:
#     if char == symb:
#         count+=1
# print(f"Кількість символів {symb} в тексті зустрічається {count} раз") 

# Завдання 3
# Користувач вводить з клавіатури рядок. Зробіть поворот рядків і отриманий результат 
# виведіть на екран. Не використовуйте зрізи (slicing) для розв'язання задачі.

# text = input("Enter text - ")
# reserved_text = ""
# for i in range(len(text) -1,-1,-1):
#     reserved_text+=text[i]
# print(reserved_text)

# Завдання 4
# Користувач вводить з клавіатури рядок і слово для пошуку. Порахуйте скільки разів у 
# рядку зустрічається шукане слово. Отримане число виведіть на екран.

# text = input("Enter text - ")
# word = input("Enter word - ")
# count = 0
# for char in text.split():
#     if char==word:
#         count+=1
# print(count)

# Завдання 5
# Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. 
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок відобразіть на екрані.

# text = input("Enter text - ")
# word = input("Enter word - ")
# word_repl = input("Enter word - ")
# new_text = text.replace(word,word_repl)
# print("Новий текст: ", new_text)



