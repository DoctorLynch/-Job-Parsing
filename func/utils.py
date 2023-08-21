import json

from classes.connector import DatabaseConnector, JsonSaver


def sorted_vacancies_by_criteria(vacancies_list: list, criteria: str) -> list:
    """
    Сортировка по заданному критерию
    """
    sorted_vacancies = []

    for job in vacancies_list:
        job_dict = job.to_dict()
        if not any(criteria.lower() in value.lower() for value in job_dict.values()):
            sorted_vacancies.append(job)

    return sorted_vacancies


def sorted_vacancies_by_keywords(vacancies_list: list, keywords: list) -> list:
    """
    Сортировка по заданным ключевым словам в описании
    """
    sorted_vacancies = []

    for job in vacancies_list:
        job_description = job.get_description()
        if job_description is not None and any(keyword.lower() in job_description.lower() for keyword in keywords):
            sorted_vacancies.append(job)

    return sorted_vacancies


def sorted_vacancies_by_salary(vacancies_list: list, desired_salary: int) -> list:
    """
    Сортировка по желаемой минимальной зарплате
    """
    desired_salary = int(desired_salary)

    sorted_vacancies = []

    for vacancy in vacancies_list:
        from_salary, to_salary = vacancy.get_salary_amount()

        if from_salary is not None and from_salary != "":
            from_salary = int(from_salary)

        from_salary = from_salary or 0

        if from_salary >= desired_salary:
            sorted_vacancies.append(vacancy)

    return sorted_vacancies


def add_vacancies_to_json_file(file_name, vacancies_list):
    """
    Добавление вакансий в джсон файл
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        data = [job.to_dict() for job in vacancies_list]
        json.dump(data, file, ensure_ascii=False, indent=2)


def remove_vacancies_from_json_file(file_name, criteria):
    job_saver = JsonSaver(file_name)

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")
        return

    for vacancy in data:
        # проверкаЮ содержит ли хотя бы одно поле критерий
        if any(criteria.lower() in str(value).lower() for value in vacancy.values()):
            job_saver.remove_vacancy(vacancy)


def get_top_vacancies(file_name: str, criteria_input: str) -> None:
    """
    Отбор топ вакансий по запросу
    """
    job_saver = JsonSaver(file_name)
    criteria_list = criteria_input.strip().split()
    criteria_jobs = job_saver.get_job(criteria_list)

    for vacancy in criteria_jobs:
        print_vacancy_info(vacancy)


def print_vacancy_info(vacancy: dict) -> None:
    """
    Краткая информация о вакансиях
    """
    title = vacancy["title"]
    url = vacancy["url"]
    salary_data = vacancy["salary_data"]

    if salary_data is not None:
        from_salary = salary_data.get("from")
        to_salary = salary_data.get("to")
        currency = salary_data.get("currency")

        if (from_salary is None or from_salary == 0) and (to_salary is None or to_salary == 0):
            salary_info = "зарплата не указана"
        elif (from_salary is None or from_salary == 0) and (to_salary is not None and to_salary != 0):
            salary_info = f"зарплата до {to_salary} {currency}"
        elif (from_salary is not None and from_salary != 0) and (to_salary is None or to_salary == 0):
            salary_info = f"зарплата от {from_salary} {currency}"
        elif (from_salary is not None and from_salary != 0) and (to_salary is not None and to_salary != 0):
            salary_info = f"зарплата от {from_salary} до {to_salary} {currency}"
    else:
        salary_info = "зарплата не указана"

    print(f"Вакансия - {title}, {salary_info}, подробная информация - {url}\n")


def get_keywords_from_user():
    """
    Получение ключевых слов для сортировки вакансий
    """
    print("Введите ключевые слова для сортировки вакансий (через пробел):")
    keywords_input = input().strip()
    keywords = keywords_input.split()
    return keywords


