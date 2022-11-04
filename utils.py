import json

def load_candidates_from_json():
    """Загружает список из файла"""
    with open("candidates.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def get_candidate(candidate_id):
    """Возвращает кандидата по id в виде словаря"""
    data = load_candidates_from_json()

    for person in data:
        if person['id'] == candidate_id:
            return person

    return None

def get_candidates_by_name(candidate_name):
    """Возвращает кандидата по имени в виде словаря"""
    data = load_candidates_from_json()
    result = []
    for person in data:

        if person['name'] == candidate_name:
            result.append(person)

    return result

def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    data = load_candidates_from_json()
    result = []

    for item in data:

        if skill_name in item['skills'].lower().split(sep=", "):
            result.append(item)

    return result

