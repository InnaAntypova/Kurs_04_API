
class Vacancy:
    """
    Класс для создания объектов-вакансий
    """
    vacancy_obj_list = []

    def __init__(self, vacancy_name: str, area: str, salary_from: int, salary_to: int, address: str, published: str,
                 requirement: str, responsibility: str, employment: str, platform: str, vacancy_url: str):
        self.vacancy_name = vacancy_name
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.address = address
        self.published = published
        self.requirement = requirement
        self.responsibility = responsibility
        self.employment = employment
        self.platform = platform
        self.vacancy_url = vacancy_url

    def __str__(self) -> str:
        """ Переопределенный метод __str__ для печати информации о вакансии """
        return f"Платформа: {self.platform}\nДата публикации: {self.published}\n" \
               f"Название вакансии: {self.vacancy_name}\nГород: {self.area}\nАдрес: {self.address}\n" \
               f"Требования: {self.requirement}\nОбязанности: {self.responsibility}\n" \
               f"Зарплата: {self.salary_from} - {self.salary_to} RUB.\nГрафик работы: {self.employment}\n" \
               f"URL:{self.vacancy_url}"

    def __repr__(self) -> str:
        """ Метод выводит информацию для разработчика """
        return f"{self.__class__.__name__}({self.vacancy_name}, {self.address}, {self.salary_from}, {self.salary_to})"

    def __gt__(self, other) -> bool:
        """ Метод для сравнения заработной платы """
        if self.salary_to != 0 and other.salary_to != 0:
            return self.salary_to > other.salary_to
        elif self.salary_to == 0:
            return self.salary_from > other.salary_to
        elif other.salary_to == 0:
            return self.salary_to > other.salary_from
