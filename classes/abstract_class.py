from abc import ABC, abstractmethod

from requests import Response

from classes.connector import DatabaseConnector


class AbstractJobParser(ABC):

    @abstractmethod
    def get_request(self) -> Response:
        """
        Получение данных с API
        """
        pass

    @staticmethod
    def get_database_connector(file_name):
        """
        Возвращает экземляр класса для подключения базе данных
        """
        return DatabaseConnector(file_name)

# hh_1 = HeadHunterAPI('python')
# hh_connector = hh_1.get_database_connector('hh.json')
# data = hh_1.get_request().json()
# hh_connector.connect_database()
# hh_connector.read_data(data['items'])
# hh_connector.write_data(data['items'])
# #  крутить это в цикле, пока не переберу все странички
# # headers = {"X-Api-App-Id": os.environ["SUPERJOB_API_KEY"]}
# #         return requests.get(self.url, headers=headers, params=self.params)
# # print(os.environ["SUPERJOB_API_KEY"])
# # hh_connector.get_data('python')

# hh_api = HeadHunterAPI("Python")
# super_job_api = SuperJobAPI("Python")
# #
# # # Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_request().json()
# hh_connector = hh_api.get_database_connector('hh.json')
# hh_connector.connect_database()
# hh_connector.insert_data(hh_vacancies['items'])
# super_job_vacancies = super_job_api.get_request().json()
# super_job_connector = super_job_api.get_database_connector('super_job.json')
# super_job_connector.connect_database()
# super_job_connector.insert_data(super_job_vacancies['objects'])


