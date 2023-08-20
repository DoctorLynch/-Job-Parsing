def get_top_vacancies(vacancies, count_vacancies):
    pass

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

class HHVacancies:

    def __init__(self, title, link, description, salary):

    def __repr__(self):
        return str

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass