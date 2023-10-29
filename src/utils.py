from src.hh_vacancies import HeadHunterAPI
from src.job_vacancies import SuperJobAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy


def get_vacancies(job_title: str):
    """ Функция получения вакансий с HeadHunter.ru и Superjob.ru """
    hh_api = HeadHunterAPI(job_title)
    superjob_api = SuperJobAPI(job_title)
    json_saver = JSONSaver(job_title)
    json_saver.save_to_json([hh_api.get_vacancy(), superjob_api.get_vacancy()])
    vacancies = json_saver.read_from_json()
    return vacancies


def read_all_vacancies():
    """ Функция выводит на экран весь список вакансий"""
    for vacancy in Vacancy.vacancy_obj_list:
        print(vacancy)
        print("")
        print("")


def sort_for_date():
    """ Функция сортирует вакансии по дате публикации """
    sorted_vacancies = sorted(Vacancy.vacancy_obj_list, key=lambda x: x.published, reverse=True)
    for vacancy in sorted_vacancies:
        print(vacancy)
        print("")
        print("")


def sort_for_salary(top_n: int):
    """ Функция сортирует вакансии по заработной плате и выводит заданное пользователем количество вакансий """
    sorted_vacancies = sorted(Vacancy.vacancy_obj_list, reverse=True)
    for vacancy in sorted_vacancies[:top_n]:
        print(vacancy)
        print("")
        print("")
