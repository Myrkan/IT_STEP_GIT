# Завдання 1
# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами:
# ● з методом count
# ● з циклом for
# Приклад:
# В “it is amazing” символ “і” зустрічається 3 рази


text = input("Введи строку: ").lower()
symbol = input("Введи символ: ").lower()

count = text.count(symbol)
print(f"Символ '{symbol}' встречается {count} раз")


text = input("Введи строку: ").lower()
symbol = input("Введи символ: ").lower()

counter = 0
for ch in text:
    if ch == symbol:
        counter += 1

print(f"Символ '{symbol}' встречается {counter} раз")


# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

text = input("Введи строку: ").lower()

length = len(text)
print(f"В строке  {text} ровно {length} символов")

if "python" in text:
    print("Тут есть слово Python")
else:
    print("Тут нет слова Python")

sh_letters = "szh"
count_sh = 0
for ch in text:
    if ch in sh_letters:
        count_sh += 1

print("Количество букв s, z, h:", count_sh)


# Завдання 3
# Користувач вводить тест. Потрібно замінити всі пробіли
# на дефіси. Виправіть помилку в коді

text = input("Введіть текст: ")

result = text.replace(" ", "-")
print(f"Змінений текст: {result}")
