import json
from src.vacancies import Vacancy


class JSONSaver:
    def __init__(self, filename: str):
        self.__filename = filename  # название файла

    @property
    def filename(self):
        return self.__filename

    def save_to_json(self, data: list):
        """ Метод для записи данных в JSON"""
        with open(f'../data/{self.__filename}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def read_from_json(self):
        """ Метод для чтения из JSON и создания объектов класса Vacancy"""
        with open(f'../data/{self.__filename}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            for vacancy in item:
                vacancy_name = vacancy['vacancy_name']
                area = vacancy['area']
                salary_from = vacancy['salary_from']
                salary_to = vacancy['salary_to']
                address = vacancy['address']
                published = vacancy['published']
                requirement = vacancy['requirement']
                responsibility = vacancy['responsibility']
                employment = vacancy['employment']
                platform = vacancy['platform']
                vacancy_url = vacancy['vacancy_url']

                Vacancy.vacancy_obj_list.append(Vacancy(vacancy_name, area, salary_from, salary_to, address, published,
                                                        requirement, responsibility, employment, platform, vacancy_url))
