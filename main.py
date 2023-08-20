import os

from classes.job_parser_classes import HeadHunterAPI, HeadHunterAPI, SuperJobAPI

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
#
# №№№№№№№№№№№№№№№№№№№№
#
#
hh_api = HeadHunterAPI("Python")
super_job_api = SuperJobAPI("Python")
#
# # Получение вакансий с разных платформ
hh_vacancies = hh_api.get_request()
super_job_vacancies = super_job_api.get_request()

#
# # Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()
