import json


def load_json():
    """Функция загружает список словарей с кандидатами из json файла"""
    with open('candidates.json', 'r', encoding='utf-8') as json_file:
        cand_list = json.load(json_file)
    return cand_list


class Candidate:
    """класс содержит в себе все параметры кандидата"""

    def __init__(self, ident, name, picture, position, gender, age, skills) -> object:
        """динамические атрибуты"""
        self.ident = ident  # порядковый идентификатор
        self.name = name  # имя
        self.picture = picture  # ссылка на изображение
        self.position = position  # профессия
        self.gender = gender  # пол
        self.age = age  # возраст
        self.skills = skills  # навыки


def page_candidate_x(person_list, x):
    """ функция, , выводящая конкретного персонажа по его id"""
    for person in person_list:
        if int(person.ident) == int(x):
            return person


def page_candidate_name(person_list, name):
    """ функция, , выводящая список объектов с похожими полями name"""
    printing_list = []
    for person in person_list:
        if name in person.name.lower().split():  # не учитываем регистр
            printing_list.append(person)
    return printing_list


def page_candidate_skill(person_list, skill):
    """ функция, , выводящая список объектов с требуемым skill"""
    printing_list = []
    for person in person_list:
        if skill in person.skills.lower().split(', '):  # не учитываем регистр
            printing_list.append(person)
    return printing_list
