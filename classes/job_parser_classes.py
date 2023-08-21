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
        return requests.get(self.url, params=self.params)


class SuperJobAPI(AbstractJobParser):

    def __init__(self, keyword):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params: dict = {
            'profession': keyword
        }

    def get_request(self) -> Response:
        headers = {"X-Api-App-Id": 'v3.r.137751704.ea89fd5b14034fa68ef2b92aa69273ee0982bad8.d6ad7a810e105accdaaf7240e11520b14e148789'}
        return requests.get(self.url, headers=headers, params=self.params)


if __name__ == '__main__':
    # hh_1 = HeadHunterAPI('python')
    # df = hh_1.get_request()
    # print(df.json())
    sj_1 = SuperJobAPI('python')
    df = sj_1.get_request()
    print(df.json())







