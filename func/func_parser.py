from classes.job_parser_classes import HeadHunterAPI, SuperJobAPI
from classes.vacancies import Vacancies


def all_from_hh(search):
    """
    Получение списка вакансий по запросу на HH
    """
    hh_api = HeadHunterAPI(search)
    vacancies = hh_api.get_request().json()

    if isinstance(vacancies, str):
        print(vacancies)  # вывод сообщение об ошибке
        return []

    else:
        vacancy_list = []

        for job_data in vacancies:
            title = job_data.get('name')
            url = job_data.get('alternate_url')
            salary_data = job_data.get('salary')
            description = job_data.get('description')
            api_url = job_data.get('url')

            job = Vacancies(title, url, salary_data, description, api_url)
            vacancy_list.append(job)

        return vacancy_list


def all_from_sj(search):
    """
    Получение списка вакансий по запросу на Super_job
    """
    sj_api = SuperJobAPI(search)
    vacancies = sj_api.get_request().json()

    if isinstance(vacancies, str):
        print(vacancies)  # сообщения об ошибке
        return []

    else:
        vacancy_list = []

        for job_data in (vacancies['objects']):
            title = job_data['profession']
            url = job_data['link']
            salary_data = {
                'from': job_data['payment_from'],
                'to': job_data['payment_to'],
                'currency': job_data['currency'],
                'gross': None
            }

            if 'client' in job_data and 'description' in job_data['client']:
                description = job_data['client']['description']
            else:
                description = ""
            api_url = None

            job = Vacancies(title, url, salary_data, description, api_url)
            vacancy_list.append(job)

        return vacancy_list