import requests
from requests import Response
from classes.abstract_class import AbstractJobParser


class HeadHunterAPI(AbstractJobParser):

    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': keyword,
            'page': 0,
            'per_page': 100,
            'search_field': 'name'
        }

    def get_request(self) -> Response:
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get('items', [])

            if not vacancies:
                return "Извините, по вашему поисковому запросу не нашлось вакансий."

            return vacancies
        else:
            return "Ошибка {response.status_code}"


class SuperJobAPI(AbstractJobParser):

    def __init__(self, keyword):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params: dict = {
            'profession': keyword
        }

    def get_request(self) -> Response:
        headers = {"X-Api-App-Id": 'v3.r.137751704.ea89fd5b14034fa68ef2b92aa69273ee0982bad8.d6ad7a810e105accdaaf7240e11520b14e148789'}
        return requests.get(self.url, headers=headers, params=self.params)







