from src.vacancies_abc import ABCVacancies
import requests
import datetime
import os


class SuperJobAPI(ABCVacancies):
    """ Класс для работы с API сайта superjob.ru """

    JOB_URL = "https://api.superjob.ru/2.0/vacancies/"
    api_key = os.getenv('JOB_API_KEY')

    def __init__(self, job_title: str):
        self.job_title = job_title  # Название вакансии

    def get_from_api(self):
        """ Метод для получения ответа от API"""

        param = {'keyword': self.job_title,
                 'town': 73,  # ищем в Ростове-на-Дону
                 'page': 0,
                 'count': 100}  # кол-во вакансий

        headers = {"X-Api-App-Id": SuperJobAPI.api_key}

        response = requests.get(url=SuperJobAPI.JOB_URL, headers=headers,
                                params=param).json()['objects']
        return response

    def get_vacancy(self) -> list:
        """ Метод собирает из необходимых данных лист с вакансиями"""
        all_job_vacancies = []
        data = self.get_from_api()
        try:
            for vacancy in data:
                published = datetime.datetime.fromtimestamp(vacancy['date_pub_to']).strftime('%d-%m-%Y')
                salary_from = vacancy['payment_from'] if vacancy['payment_from'] else 0
                salary_to = vacancy['payment_to'] if vacancy['payment_to'] else 0
                address = vacancy['address'] if vacancy['address'] else ''
                all_job_vacancies.append({
                    'address': address,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'published': published,
                    'vacancy_url': vacancy['link'],
                    'vacancy_name': vacancy['profession'],
                    'area': vacancy['town']['title'],
                    'employment': vacancy['type_of_work']['title'],
                    'requirement': vacancy['vacancyRichText'],
                    'responsibility': '',
                    'platform': 'SuperJob'})

            if not all_job_vacancies:
                raise ValueError

            return all_job_vacancies

        except ValueError:
            raise ValueError('Ошибка данных.')
