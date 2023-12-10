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
    contact_num = int(input('Укажите порядковый номер контакта, который хотите скопировать или нажмите 0 для выхода: '))

    if contact_num == 0:
            print()
            return
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')
        contact_for_copy = contacts_list[contact_num - 1] + '\n\n'

    while contact_num > len(contacts_list):
        if contact_num == 0:
            print()
            return
        print('Контакта с таким порядковым номером не существует!')
        contact_num = int(input('Укажите порядковый номер контакта, который хотите скопировать или нажмите 0 для выхода: '))

    with open('new_phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_for_copy)
        print('Контакт скопирован!\n')


def delete_contact():
    print_contacts()
    contact_num = int(input('Укажите порядковый номер контакта, который хотите удалить из справочника или нажмите 0 для выхода: '))

    if contact_num == 0:
            print()
            return
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')

    while contact_num > len(contacts_list):
        if contact_num == 0:
            print()
            return
        print('Контакта с таким порядковым номером не существует!')
        contact_num = int(input('Укажите порядковый номер контакта, который хотите удалить из справочника или нажмите 0 для выхода: '))

    contacts_list.pop(contact_num - 1)
    contacts_str = ''

    for element in contacts_list:
        contacts_str += element + '\n\n'

    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(contacts_str)

    print('Контакт успешно удален!')
    print()


def edit_contact():
    print_contacts()
    contact_num = int(input('Укажите порядковый номер контакта, который хотите отредактировать или нажмите 0 для выхода: '))

    if contact_num == 0:
            print()
            return
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')

    while contact_num > len(contacts_list):
        if contact_num == 0:
            print()
            return
        print('Контакта с таким порядковым номером не существует!')
        contact_num = int(input('Укажите порядковый номер контакта, который хотите отредактировать или нажмите 0 для выхода: '))

    print()
    contact_list = contacts_list[contact_num - 1].replace('\n', ' ').split(' ')
    print(*contact_list)
    print()
    
    print('Варианты редактирования:\n'
        '1. Фамилия\n'
        '2. Имя\n'
        '3. Отчество\n'
        '4. Телефон\n'
        '5. Город проживания\n'
        '6. Выход из редактирования\n'
    )

    edit_num = int(input('Введите номер варианта для редактирования: '))

    if edit_num == 6:
        print()
        return
    
    while edit_num not in (1, 2, 3, 4, 5):
            print('Некорректный ввод.')
            edit_num = input('Введите номер варианта для редактирования: ')

    contact_list[edit_num - 1] = ''
    contact_list[edit_num - 1] = input('Введите новое значение: ')
    print(*contact_list)
    print('Контакт отредоктирован!')
    print()
    contact_str = ''

    for i in range(len(contact_list)):
        if i == 3:
            contact_str += contact_list[i] + '\n'
        else:
             contact_str += contact_list[i] + ' '

    contacts_list[contact_num - 1] = contact_str
    contacts_str = ''

    for element in contacts_list:
        contacts_str += element + '\n\n'

    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(contacts_str)