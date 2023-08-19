import requests
from requests import Response

from classes.abstract_class import AbstractJobParser


class HH(AbstractJobParser):

    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.params: dict = {
            'text': keyword,
            'page': 0,
            'per_page': 100,
            'search_field': 'name'
        }

    def get_request(self) -> Response:
        return requests.get(self.url, params=self.params)





if __name__ == '__main__':
    hh_1 = HH('python')
    df = hh_1.get_request()
    print(df.json())







