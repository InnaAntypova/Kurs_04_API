from src.vacancies_abc import ABCVacancies
import requests
from datetime import datetime
from src.vacancies import Vacancy


class HeadHunterAPI(ABCVacancies):
    """ Класс для работы с API сайта hh.ru """

    HH_url = "https://api.hh.ru/vacancies"

    def __init__(self, job_title: str):
        self.job_title = job_title  # Название вакансии

    def get_vacancies(self):
        """ Метод для получения вакансий """

        param = {'text': self.job_title,
                 'area': 76,  # ищем в Ростове-на-Дону
                 'page': 0,
                 'per_page': 100}  # кол-во вакансий

        response = requests.get(url=HeadHunterAPI.HH_url, headers={"User-Agent": "HH-User-Agent"}, params=param).json()

        vacancies_list = []
        for item in response['items']:
            vacancies_list.append(item)

        return vacancies_list

    def __repr__(self):
        return self.job_title

    @staticmethod
    def get_vacancy(vacancies_list):
        for vacancy in vacancies_list:
            if vacancy['address']:
                address = vacancy['address']['raw']
            else:
                address = vacancy['address']

            vacancy_name = vacancy['name']
            area = vacancy['area']['name']
            employment = vacancy['employment']['name']
            id_v = vacancy['id']
            published = vacancy['published_at']
            requirement = vacancy['snippet']['requirement']
            responsibility = vacancy['snippet']['responsibility']

            if vacancy['salary']:
                salary = f"{vacancy['salary']['from']} - {vacancy['salary']['to']} {vacancy['salary']['currency']}"
            else:
                salary = vacancy['salary']

            vacancy = Vacancy(vacancy_name, area, salary, address, published, requirement, responsibility,
                              employment, id_v)
            Vacancy.vacancy_obj_list.append(vacancy)


# hh = HeadHunterAPI('Python')
# print(hh.get_vacancies())
# print(len(hh.get_vacancies()))
