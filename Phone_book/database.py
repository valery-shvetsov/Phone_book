import json

# Создаём новый файл .json, если не найдет с указанным именем.
def create_json():
    """
    Функция проверяет, существует ли файл phone_file.json, если нет, то создаёт
    и располагает там пустой список json_data = [].
    """
    json_data = []
    with open('phone_file.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))


# Добавляем в массив файла новый контакт. Надо сделать русский язык!
def add_to_json(contact):
    """
    Функция добавляет в массив файла новый контакт

    Args:
        Создаём объект json, функция считывает 
        его под видом переменной contact и добавляет в список в файле phone_file.json
    """
    card = json.load(open('phone_file.json'))
    card.append(contact)
    with open("phone_file.json", "w", encoding = 'utf-8') as file:
        return json.dump(card, file, indent=4, ensure_ascii=False)

contact_1 = {
    "id": 1,
    "sec_name": 'Тюрин', 
    "first_name": 'Роман',
    "tel_number": '+71238760789',
    "adress": 'Нижний Новгород'
}

contact_2 = {
    "id": 2,
    "sec_name": '', 
    "first_name": 'ufviuc',
    "tel_number": '+71938760789',
    "adress": 'lvjhvjhvljvh'
}

contact_3 = {
    "id": 3,
    "sec_name": 'Чернов', 
    "first_name": 'Владимир',
    "tel_number": '+71238760789',
    "adress": 'Минск'
}


# Считываем записанный файл 
def read_file():
    """
    Функция считывает из файла объекты json 
    и выводит их в виде списка.

    Returns:
        _type_: _description_
    """
    with open("phone_file.json", "r", encoding = 'utf-8') as read_file:
        return print(f'{json.load(read_file)}' + '\n')

# create_json()

# add_to_json(contact_1)
# add_to_json(contact_2)
add_to_json(contact_3)

# read_file()

# exit()
