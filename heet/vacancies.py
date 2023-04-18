"""Класс для работы с вакансиями"""


class Vacancy:
    def __init__(self, title, salary, description, url):
        self.title = title
        self.salary = salary
        self.description = description
        self.url = url

    def __str__(self):
        return f'title: {self.title}, salary: {self.salary}, description: {self.description}, url: {self.url}'
