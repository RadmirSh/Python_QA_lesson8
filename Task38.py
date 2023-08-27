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


def show_contacts(book: dict, message: str):
    print('\n' + '=' * 67)
    if book:
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    else:
        print(message)
    print('=' * 67 + '\n')



def add_new_contact(book: dict, new: list):
    cur_id = max(book.keys()) + 1
    book[cur_id] = new


def find_contact(book: dict, search: str):
    resault = {}
    for i, contact in book.items():
        for field in contact:
            if search.lower() in field.lower():
                resault[i] = contact
                break
    return resault