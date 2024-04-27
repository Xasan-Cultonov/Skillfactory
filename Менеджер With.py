try:
    with open('text.txt', 'r', encoding='ufr-8') as file:
        print(file.read())
except FileExistsError:
    print("Файл не найден")


