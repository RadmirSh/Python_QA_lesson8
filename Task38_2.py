import os, re

# редактирование номера под необходимый формат
def phone_format(n):  
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]

# вывод в консоль справочника
def printData(data):  
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Фамилия        Имя          Номер")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "lastName": lastName,
                "name": name,
                "phone": phone_format(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)

# открытие телефонной книги
def showContacts(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- нажмите любую кнопку ---")


# добавление нового контакта
def addContact(fileName):  
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Фамилия: ") + ","
        res += input("Имя: ") + ","
        res += input("Телефонный номер: ")

        file.write(res + "\n")

    input("\nКонтакт добавлен!\n--- нажмите любую кнопку ---")

# поиск контактов
def findContact(fileName):  
    os.system("cls")
    target = input("Введите данные для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                

    if len(result) != 0:
        printData(result)
    else:
        print(f"Нет такого контакта '{target}'.")

    input("--- нажмите любую кнопку ---")

# изменение информации в контакте
def changeContact(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для изменения или 0 для возврата в меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Новая фамилия: ")
            newName = input("Новое имя: ")
            newPhone = input("Новый номер: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт изменен!")
                input("\n--- нажмите любую кнопку ---")
        else:
            return

# удаление контакта 
def deleteContact(fileName):  
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для его удаления или 0 для возврата в меню: ")
        )
        if numberContact != 0:
            print(f"Запись об удалении: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- нажмите любую кнопку ---")

# отрисовка интерфейса главного меню
def drawInterface():  
    print("#####   ТЕЛЕФОННЫЙ СПРАВОЧНИК   #####")
    print("=" * 26)
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавить контакт")
    print(" [3] -- Найти контакт")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")
    print("=" * 26)

# реализация главного меню
def main(file_name):  
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите значение от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо")
            return


path = "phonebook.txt"

main(path)