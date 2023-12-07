from date_create import *

def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
    print('\nКонтакт записан!\n')


def print_contacts():
    # '''List all entries'''
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     print('-----------------------')
    #     print(file.read())
    #     print('-----------------------')

#2 
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(f'{nn}. {contact}\n')


def search_contact(field=''):
    print(
    'Возможные варианты поиска:\n'
    '1. по фамилии\n'
    '2. по имени\n'
    '3. по отчеству\n'
    '4. по номеру\n'
    '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))-1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

        contacts_list = contacts_str.rstrip().split('\n\n')
    # print(contacts_list)

    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')


def copy_contact():
    print_contacts()
    contact_num = int(input('Укажите порядковый номер контакта, который хотите скопировать: '))
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')

    while contact_num > len(contacts_list):
        print('Контакта с таким порядковым номером не существует!')
        contact_num = int(input('Укажите порядковый номер контакта, который хотите скопировать: '))

        contact_for_copy = contacts_list[contact_num - 1]

    with open('new_phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_for_copy)
        print('Контакт скопирован!')