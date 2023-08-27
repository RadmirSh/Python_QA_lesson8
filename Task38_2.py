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
    print(" №  Lastname        Name          Phone Numbers")
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
    input("\n--- press any key ---")


# добавление нового контакта
def addContact(fileName):  
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Input a Surname of Contact: ") + ","
        res += input("Input a Name of Contact: ") + ","
        res += input("Input a Phone Number of Contact: ")

        file.write(res + "\n")

    input("\nContact was successfully added!\n--- press any key ---")

# поиск контактов
def findContact(fileName):  
    os.system("cls")
    target = input("Input Item of Contact for searching: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                

    if len(result) != 0:
        printData(result)
    else:
        print(f"There is no Contact with this Item '{target}'.")

    input("--- press any key ---")

# изменение информации в контакте
def changeContact(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Input Number of Contact for changing or 0 for return Main Menu: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Input new Lastname: ")
            newName = input("Input new Name: ")
            newPhone = input("Input new Phone: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nContact was successfully changed!")
                input("\n--- press any key ---")
        else:
            return

# удаление контакта 
def deleteContact(fileName):  
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Input Number of Contact for deleting or 0 for return Main Menu: ")
        )
        if numberContact != 0:
            print(f"Deleting record: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- press any key ---")

# отрисовка интерфейса главного меню
def drawInterface():  
    print("#####   PHONE BOOK   #####")
    print("=" * 26)
    print(" [1] -- Show Contacts")
    print(" [2] -- Add Contacts")
    print(" [3] -- Find Contacts")
    print(" [4] -- Change Contacts")
    print(" [5] -- Delete Contacts")
    print("\n [0] -- Exit")
    print("=" * 26)

# реализация главного меню
def main(file_name):  
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Input a Number for 1 to 5 or 0 for Exit: "))

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
            print("Thank you!")
            return


path = "phonebook.txt"

main(path)