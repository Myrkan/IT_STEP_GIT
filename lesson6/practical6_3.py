# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат

numbers = [1, 8, -5, 9]

print("Начальный список:")
for num in numbers:
    print(num)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 3
print("После умножения на 3:", numbers)

for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = 0
print("После замены чисел > 10 на 0:", numbers)


# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

numbers = []

while True:
    num = int(input("Введите число (-1-выход): "))
    if num == -1:
        break
    numbers.append(num)

print("Количество чисел:", len(numbers))
print("Сумма:", sum(numbers))
print("Минимальное:", min(numbers))
print("Максимальное:", max(numbers))
print("Среднее:", sum(numbers) / len(numbers))


# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

while True:
    number = int(input("Введіть число (0 для завершення): "))

    positive = []
    negative = []

    if number < 0:
        positive.append(number)
    else:
        negative.append(number)

print("Додатні числа:", positive)
print("Від'ємні числа:", negative)

# исправление

positive = []  # создаем списки один раз, а не каждый цикл
negative = []

while True:
    number = int(input("Введіть число (0 для завершення): "))

    if number == 0:  # 0 — добавляем для выхода
        break

    if number > 0:  # положительные-только > 0
        positive.append(number)
    else:  # здесь будут только отрицательные <0
        negative.append(number)

print("Додатні числа:", positive)
print("Від'ємні числа:", negative)

# Завдання 4
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати

salaries = []

while True:
    salary = float(input("Введите зарплату (-1 для выхода): "))
    if salary == -1:
        break
    salaries.append(salary)

percent = float(input("Введите процент повышения: "))

for i in range(len(salaries)):
    salaries[i] = salaries[i] + salaries[i] * percent / 100

print("Новые зарплаты:")
for salary in salaries:
    print(salary)
