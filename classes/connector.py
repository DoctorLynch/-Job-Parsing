import json
import os


class DatabaseConnector:
    def __init__(self, file_path):
        self.file_path = file_path

    def connect_database(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)


class JsonSaver(DatabaseConnector):
    def read_data(self):
        """
        Читаем
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def write_data(self, data):
        """
        Записываем
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # def insert_data(self, data):
    #     with open(self.file_path, 'r') as file:
    #         data_dict = json.load(file)
    #         new_data_dict = data_dict + data
    #     with open(self.file_path, 'w') as file:
    #         json.dump(new_data_dict, file, indent=4, ensure_ascii=False)

    def get_job(self, criteria_list):
        """
        Поиск вакансий, соответствующих определенным критериям
        """
        data = self.read_data()

        criteria_jobs = []

        for job in data:
            for value in job.values():
                # проверка, является ли значение строкой и удовлетворяет ли хотя бы одному критерию
                if any(isinstance(value, str) and criteria.lower() in value.lower() for criteria in criteria_list):
                    criteria_jobs.append(job)
                    break

        return criteria_jobs

    def add_job(self, job) -> None:
        """
        Добавления новой записи о вакансии
        """
        data = self.read_data()
        new_data = data + job  # преобразование объекта в словарь перед добавлением, используется метод класса Vacancies
        self.write_data(new_data)

    def remove_job(self, job) -> None:
        """
        Удаления записи из списка данных
        """
        data = self.read_data()
        new_data = []

        for item in data:
            if item != job:
                new_data.append(item)
        self.write_data(new_data)




if __name__ == '__main__':
    ins_1 = DatabaseConnector('as.json')
    ins_1.connect_database()
