print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня")

while True:
    print("1. Отримати книжку")
    print("2. Повернути книжку")
    print("3. Вихід")
    choice = input("Оберіть дію: ")
    if choice == "3":
        break
    elif choice == "1" or choice == "2":
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книжки: ")
        if name == "" or book == "":
            print("Помилка: ім'я та назва книжки не можуть бути порожніми!")
            continue
        if choice == "1":
            days = int(input("На скільки днів: "))
            if days <= 0 or days > 30:
                print("Помилка: кількість днів має бути від 1 до 30!")
                continue
            print(f"Книжку {book} видано читачеві {name} на {days} днів")
        elif choice == "2":
            print(f"Читач {name} повернув книжку {book}")
    else:
        print("Невірний вибір, спробуйте ще раз")
