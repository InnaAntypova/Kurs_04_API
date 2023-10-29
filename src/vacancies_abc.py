from abc import ABC, abstractmethod


class ABCVacancies(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями."""

    @abstractmethod
    def get_from_api(self):
        """
        Метод для получения вакансий от API
        """
        pass

