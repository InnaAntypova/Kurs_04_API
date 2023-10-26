from src.vacancies_abc import ABCVacancies
import requests
import os
from src.vacancies import Vacancy


class SuperJobAPI(ABCVacancies):
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

        response = requests.get(url=SuperJobAPI.JOB_URL, headers={"X-Api-App-Id": SuperJobAPI.api_key},
                                params=param).json()
        # vacancies_list = []
        # for item in response['objects']:
        #     vacancies_list.append(item)
        # return vacancies_list
        return response

    @staticmethod
    def get_vacancy(response_data):
        for vacancy in response_data['objects']:
        #for vacancy in response_data:
            address = vacancy['address']
            vacancy_name = vacancy['profession']
            area = vacancy['town']['title']
            employment = vacancy['type_of_work']['title']
            id_v = vacancy['id']
            published = vacancy['date_pub_to']
            requirement = vacancy['vacancyRichText']
            responsibility = None
            salary = f"{vacancy['payment_from']} - {vacancy['payment_to']} {vacancy['currency']}"

            vacancy = Vacancy(vacancy_name, area, salary, address, published, requirement, responsibility,
                              employment, id_v)
            Vacancy.vacancy_obj_list.append(vacancy)

# job = SuperJobAPI('Python')
# print(job.get_vacancies())


