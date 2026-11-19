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
