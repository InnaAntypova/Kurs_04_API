import json
import os


class JSONSaver:
    def __init__(self):
        pass

    @staticmethod
    def save_to_json(data):
        with open('../data/vacancies_json.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, sort_keys=True, indent=2)

