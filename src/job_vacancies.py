from src.vacancies import Vacancies
import requests
import os


class JOBVacancies(Vacancies):
    """ Класс для работы с API сайта superjob.ru """

    JOB_URL = "https://api.superjob.ru/2.0/vacancies/"
    #api_key = os.getenv('JOB_API_KEY')
    api_key = "v3.r.137907415.84f7e50b55699620c59a13a1344f0facc53c2fdf.678f1650d10037c5e5814687c5e8b7a13b76ee57"

    def __init__(self, job_title: str):
        self.job_title = job_title  # Название вакансии

    def get_vacancies(self):
        """ Метод для получения вакансий """

        param = {'keyword': self.job_title,
                 'town': 73,  # ищем в Ростове-на-Дону
                 'page': 0,
                 'count': 100}  # кол-во вакансий

        response = requests.get(url=JOBVacancies.JOB_URL, headers={"X-Api-App-Id": JOBVacancies.api_key},
                                params=param).json()
        return response


job = JOBVacancies('Python')
print(job.get_vacancies())


