print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня")

while True:
    print("1. Отримати книжку")
    print("2. Повернути книжку")
    print("3. Вихід")
    choice = input("Оберіть дію: ")
    if choice == "3":
        break
    if choice == "1" or choice == "2":
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книжки: ")
        if choice == "1":
            days = int(input("На скільки днів: "))
            print(f"Книжку {book} видано читачеві {name} на {days} днів")
        elif choice == "2":
            print(f"Читач {name} повернув книжку {book}")
