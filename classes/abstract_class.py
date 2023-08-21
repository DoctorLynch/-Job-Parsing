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

