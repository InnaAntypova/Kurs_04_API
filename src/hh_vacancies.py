from src.vacancies import Vacancies
import requests
import json


class HHVacancies(Vacancies):
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

        response = requests.get(url=HHVacancies.HH_url, headers={"User-Agent": "HH-User-Agent"}, params=param).json()
        return response

    def __repr__(self):
        return self.job_title


hh = HHVacancies('Python')
print(hh.get_vacancies())
