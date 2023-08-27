phone_book = {}
PATH = 'phones.txt'


def open_file(book: list):
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        book[i] = contact


def save_file(book: dict):
    all_contacts = []
    for contact in book.values():
        all_contacts.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(all_contacts))