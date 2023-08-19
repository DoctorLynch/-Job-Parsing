import json
import os


class DatabaseConnector:
    def __init__(self, file_path):
        self.file_path = file_path

    def connect_database(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def insert_data(self, data):
        with open(self.file_path, 'r') as file:
            data_dict = json.load(file)
            new_data_dict = data_dict + data
        with open(self.file_path, 'w') as file:
            json.dump(new_data_dict, file, indent=4, ensure_ascii=False)

    #  написать метод для получения данных из джейсон файла по запросу
    #  метод для удаления данных


if __name__ == '__main__':
    ins_1 = DatabaseConnector('as.json')
    ins_1.connect_database()

    # def get_job(self, criteria: List) -> list:
    #     """
    #     Поиск вакансий, соответствующих определенным критериям
    #     """
    #     pass
    #
    # def add_job(self, job) -> None:
    #     """
    #     Добавление новой записи о вакансии
    #     """
    #     pass
    #
    # def remove_job(self, job) -> None:
    #     """
    #     Удаление записи из списка данных
    #     """
    #     pass