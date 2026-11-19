print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня")

while True:
    print("1. Отримати книжку")
    print("2. Вихід")
    choice = input("Оберіть дію: ")
    if choice == "1":
        name = input("Введіть ваше ім'я: ")
        book = input("Введіть назву книжки: ")
        print(f"Книжку {book} видано читачеві {name}")
    elif choice == "2":
        break
