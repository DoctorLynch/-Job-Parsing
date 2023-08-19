import requests
from typing import Dict, Union
from classes.abstract_class import AbstractJobParser


class SuperJob(AbstractJobParser):

    def __init__(self):
        self.base_url = "https://api.superjob.ru/2.0/vacancies/"
        self.secret_key ='v3.r.137751704.ea89fd5b14034fa68ef2b92aa69273ee0982bad8.d6ad7a810e105accdaaf7240e11520b14e148789'

    def connect(self) -> Dict:
        """
        Метод для подключения к API
        """
        headers = {"X-Api-App-Id": self.secret_key}
        response = requests.get(self.base_url, headers=headers)
        response.raise_for_status()  # проверка на ошибки
        return response.json()

    def get_vacancies(self, search_query: str) -> Union[Dict, str]:
        """
        Получение вакансий по запросу
        """
        url = f"{self.base_url}?keyword={search_query}"
        headers = {"X-Api-App-Id": self.secret_key}

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки в запросе
        data = response.json()

        if not data.get('objects'):
            return "Извините, по вашему поисковому запросу не нашлось вакансий."
        return data

