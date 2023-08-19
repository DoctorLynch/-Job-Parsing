import os

from classes.job_parser_classes import HH

hh_1 = HH('python')
hh_connector = hh_1.get_database_connector('hh.json')
data = hh_1.get_request().json()
hh_connector.connect_database()
hh_connector.insert_data(data['items'])
#  крутить это в цикле, пока не переберу все странички
# headers = {"X-Api-App-Id": os.environ["SUPERJOB_API_KEY"]}
#         return requests.get(self.url, headers=headers, params=self.params)
# print(os.environ["API"])
hh_connector.get_data()


