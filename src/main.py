from src.hh_vacancies import HeadHunterAPI
from src.job_vacancies import SuperJobAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy

def main():
    print("Программа сформирует для Вас список вакансий из таких платформ: 'HeadHunter', 'SuperJob'")
    job_title = str(input("Введите данные для поиска: ")).title()
    # hh_api = HeadHunterAPI(job_title)
    # hh_vacan = hh_api.get_vacancies()
    # hh_api.get_vacancy(hh_vacan)
    # vacancy = Vacancy
    # vacancy.vacancy_info()

    superjob_api = SuperJobAPI(job_title)
    vac = superjob_api.get_vacancies()
    superjob_api.get_vacancy(vac)
    vacancy = Vacancy
    vacancy.vacancy_info()




if __name__ == '__main__':
    main()