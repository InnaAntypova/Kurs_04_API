
class Vacancy:
    """
    Класс для создания объектов-вакансий
    """
    vacancy_obj_list = []

    def __init__(self, vacancy_name, area, salary, address, published, requirement, responsibility, employment, id_v):
        self.vacancy_name = vacancy_name
        self.area = area
        self.salary = salary
        self.address = address
        self.published = published
        self.requirement = requirement
        self.responsibility = responsibility
        self.employment = employment
        self.id_v = id_v

    def __str__(self):
        return f"{self.vacancy_name},{self.area}, {self.salary}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.vacancy_name},{self.area}, {self.salary})"

    @staticmethod
    def vacancy_info():
        for vacancy in Vacancy.vacancy_obj_list:
            print("")
            print(f"ID вакансии: {vacancy.id_v}\nДата публикации: {vacancy.published}\n"
                  f"Название вакансии: {vacancy.vacancy_name}\nГород: {vacancy.area}\nАдрес: {vacancy.address}\n"
                  f"Требования: {vacancy.requirement}\nОбязанности: {vacancy.responsibility}\n"
                  f"Зарплата: {vacancy.salary}\nГрафик работы: {vacancy.employment}")
            print("")


