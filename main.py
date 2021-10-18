documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def main(doc, dir):
    while True:
        print(documents)
        print(directories)
        user_input = input('Введите команду или q для выхода :')
        if user_input == 'p':
            owner_doc()
        elif user_input == 's':
            find_shelf()
        elif user_input == 'l':
            list_doc()
        elif user_input == 'a':
            add_doc()
        elif user_input == 'd':
            del_doc()
        elif user_input == 'as':
            new_shelv()
        elif user_input == 'm':
            move_doc()
        elif user_input == 'q':
            print('Приходите ещё...')
            break


def move_doc():
    number_doc = input('Введите номер премещаемого документа: ')
    number_shelv = input('Введите номер целевой полки: ')
    count = 0
    if number_shelv not in directories:
        print('Нeт полки с таким номером! Сначала создайте такую полку!')
        return
    else:
        for num_s, num_d in directories.items():
            if number_doc in num_d:
                num_d.remove(number_doc)
                break
    if number_shelv in directories:
        directories[number_shelv].append(number_doc)
    else:
        directories[number_shelv] = [number_doc]
    print(f'Документ {number_doc} перемещён на полку {number_shelv} ')


def new_shelv():
    new_num = input('Введите новый номер полки')
    if new_num in directories:
        print("Такая полка уже есть!!!")
    else:
        directories[new_num] = []


def del_doc():
    number_doc = input('Введите номер документа для удаления: ')
    for doc in documents:
        if doc['number'] == number_doc:
            documents.remove(doc)
    for num_s, num_d in directories.items():
        if number_doc in num_d:
            num_d.remove(number_doc)
            break


def owner_doc():
    find_doc = input('Введите номер документа: ')
    count = 0
    for doc in documents:
        if doc["number", 0] == find_doc:
            print(f'Владелец документа {find_doc}: {doc["name"]}')
            count += 1
    if count == 0:
        print(f'Документ {find_doc} не найден')


def find_shelf():
    find_doc = input('Введите номер документа: ')
    count = 0
    for shelf, doc in directories.items():
        for doc_f in doc:
            if doc_f == find_doc:
                print(f'Полка документа {find_doc}: {shelf}')
                count += 1
    if count == 0:
        print(f'Документ {find_doc} не найден')


def list_doc():
    for doc in documents:
        print(f'{doc["type"]} {doc["number"]} {doc["name"]}')


def add_doc():
    type_doc = input('Введите тип документа: ')
    number_doc = input('Введите номер документа: ')
    owner_doc = input('Введите владельца: ')
    num_shelv = input('Введите номер полки: ')
    if type_doc and number_doc and owner_doc and num_shelv:
        documents.append({"type": type_doc, "number": number_doc, "name": owner_doc})
        if num_shelv in directories:
            directories[num_shelv].append(number_doc)
        else:
            directories[num_shelv] = [number_doc]
    else:
        print('ВВедены не все данные!!!')


main(documents, directories)