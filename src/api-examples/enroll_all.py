import environ, requests, os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR.parent, '.env'))

username = env('ALUNO_NAME')
password = env('PASSWORD')

base_url = 'http://localhost:8000/api/'

r = requests.get(f'{base_url}courses/') # obtém todos os cursos
courses = r.json()

available_courses = ', '.join([course['title'] for course in courses])
print(f'Available courses: {available_courses}')

for course in courses:
    # cadastra o aluno em todos os cursos
    course_id = course['id']
    course_title = course['title']
    r = requests.post(
        f'{base_url}courses/{course_id}/enroll/',
        auth=(username, password)
    )

    print(f'Cadastrando no curso {course_title}')

    if r.status_code == 200:
        print(f'Successfully enrolled in {course_title}')
