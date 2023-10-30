from src.utils import get_vacancies, read_all_vacancies, sort_for_date, sort_for_salary


def main():
    print("Программа сформирует для Вас список вакансий из таких платформ: 'HeadHunter', 'SuperJob'")
    job_title = str(input("Введите данные для поиска: ")).title()
    get_vacancies(job_title)
    print("Данные сформированы.")
    while True:
        print("Нажмите '1' - для чтения всех вакансий, '2' - отсортировать по дате, '3' - топ N вакансий по зарплате.")
        print("Для завершения программы нажмите '0'.")
        user_input = input("Ваш выбор: ")
        print("")

        if user_input == '1':
            read_all_vacancies()

        if user_input == '2':
            print('\n' * 100)
            sort_for_date()

        if user_input == '3':
            top_n = int(input("Введите количество вакансий: "))
            print('\n' * 100)
            sort_for_salary(top_n)

        if user_input == '0':
            print("Программа завершена.")
            break


if __name__ == '__main__':
    main()
