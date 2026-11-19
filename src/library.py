print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня")

while True:
    print("1. Отримати книжку")
    print("2. Повернути книжку")
    print("3. Вихід")
    choice = input("Оберіть дію: ")
    if choice == "1":
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книжки: ")
        days = int(input("На скільки днів: "))
        print(f"Книжку {book} видано читачеві {name} на {days} днів")
    elif choice == "2":
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книжки: ")
        print(f"Читач {name} повернув книжку {book}")
    elif choice == "3":
        break
