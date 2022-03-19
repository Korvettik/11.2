from flask import Flask, render_template
from utils import Candidate, load_json, page_candidate_x, page_candidate_skill, page_candidate_name

app = Flask(__name__)

candidats_list = load_json()  # сразу подгрузили список словарей кандидатов

person_list = []  # создадим пустой список персонажей - объектов
for candidate in candidats_list:
    ident = candidate['id']
    name = candidate['name']
    picture = candidate['picture']
    position = candidate['position']
    gender = candidate['gender']
    age = candidate['age']
    skills = candidate['skills']
    person = Candidate(ident, name, picture, position, gender, age, skills)
    person_list.append(person)


@app.route('/', methods=['GET', 'POST'])  # главная страница, выводящая список всех персонажей (шаблон list.html)
def main_page():
    return render_template('list.html',
                           person_list=person_list)



@app.route('/candidate/<int:x>/', methods=['GET', 'POST'])  # страница, выводящая конкретного кандидата по его id (
# шаблон single.html)
def main_candidate_x(x):
    print_person = page_candidate_x(person_list, x)
    #return '<pre>' + print_person.name + '<pre>'
    return render_template('single.html',
                           person=print_person)


@app.route('/skill/<skill>/',
           methods=['GET', 'POST'])  # страница, выводящая список кандидатов, у которых содержится конкретный навык (шаблон skill.html)
def main_candidate_skill(skill):
    print_list = page_candidate_skill(person_list, skill)
    count = len(print_list)
    return render_template('skill.html',
                           persons_print_list=print_list,
                           count=count,
                           skill=skill)


@app.route('/search/<candidate_name>/',
           methods=['GET', 'POST'])  # страница, выводящая список кандидатов, у которых похожи имена (шаблон search.html)
def main_candidate_search(candidate_name):
    print_list = page_candidate_name(person_list, candidate_name)
    count = len(print_list)
    return render_template('search.html',
                           persons=print_list,
                           count=count)


if __name__ == '__main__':
    app.run(debug=True)
