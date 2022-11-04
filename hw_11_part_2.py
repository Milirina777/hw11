# Импортируем Flask и функции из файла
from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

# Создаём экземпляр/приложение Flaska - app
app = Flask(__name__)


# Используем метод приложения, регистрирующий маршрут к главной странице со списком всех кандидатов
@app.route('/')

def main_page():
    """Показываем всех кандидатов на главной странице"""

    data_candidates = load_candidates_from_json()
    return render_template("list.html", data_candidates=data_candidates)


# Теперь делаем вьюшку на страницы кандидатов
@app.route('/candidate/<int:person_id>')

def candidate_page(person_id):
    """Ссылаемся на страницы кандидатов с главной страницы"""

    info_of_candidate = get_candidate(person_id)
    return render_template("single.html", info_of_candidate=info_of_candidate)


# Теперь делаем вьюшку на поиск кандидата по имени
@app.route('/search/<candidate_name>')

def candidate_name_page(candidate_name):
    """Показываем список и количество кандидатов на странице по поиску имени"""

    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)

# Делаем вьюшку на поиск кандидатов по навыку
@app.route('/skills/<skill_name>')

def skill_name_page(skill_name):
    """Показываем список и количество кандидатов на странице по поиску имени"""

    candidate_skill_name = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidate_skill_name=candidate_skill_name)


app.run(host="127.0.0.1", port=8000, debug=True)
