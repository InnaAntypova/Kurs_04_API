from src.vacancies_abc import ABCVacancies
import requests
from datetime import datetime


class HeadHunterAPI(ABCVacancies):
    """ Класс для работы с API сайта hh.ru """

    HH_url = "https://api.hh.ru/vacancies"

    def __init__(self, job_title: str):
        self.job_title = job_title  # Название вакансии

    def get_from_api(self):
        """ Метод для получения ответа от API """
        param = {'text': self.job_title,
                 'area': 76,  # ищем в Ростове-на-Дону
                 'page': 0,
                 'per_page': 100}  # кол-во вакансий

        headers = {"User-Agent": "HH-User-Agent"}

        response = requests.get(url=HeadHunterAPI.HH_url, headers=headers, params=param).json()['items']
        return response

    def get_vacancy(self) -> list:
        """ Метод собирает из необходимых данных лист с вакансиями"""
        all_hh_vacancies = []
        data = self.get_from_api()
        try:
            for vacancy in data:
                if vacancy['salary']:
                    salary_from = vacancy['salary']['from'] if vacancy['salary']['from'] else 0
                    salary_to = vacancy['salary']['to'] if vacancy['salary']['to'] else 0
                else:
                    salary_from = 0
                    salary_to = 0

                if vacancy['address']:
                    address = vacancy['address']['raw'] if vacancy['address']['raw'] else ''
                else:
                    address = ''

                published = datetime.fromisoformat(vacancy['published_at']).strftime('%d-%m-%Y')
                responsibility = vacancy['snippet']['responsibility'] if vacancy['snippet']['responsibility'] else ''
                requirement = vacancy['snippet']['requirement'] if vacancy['snippet']['requirement'] else ''
                all_hh_vacancies.append({
                    'address': address,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'published': published,
                    'vacancy_url': vacancy['alternate_url'],
                    'vacancy_name': vacancy['name'],
                    'area': vacancy['area']['name'],
                    'employment': vacancy['employment']['name'],
                    'requirement': requirement,
                    'responsibility': responsibility,
                    'platform': 'HeadHunter'
                })

            if not all_hh_vacancies:
                raise ValueError

            return all_hh_vacancies

        except ValueError:
            raise ValueError('Ошибка данных.')
