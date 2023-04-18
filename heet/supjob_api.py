"""Работа класса, для работы с ресурсом SupJob.ru"""
import os
import requests
from heet.working_with_API import Working
from heet.vacancies import Vacancy


class SJAPI(Working):
    def __init__(self):
        self.api_key: str = os.getenv('SJ_API_KEY')
        self.headers = {'X-Api-App-ID': self.api_key}
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, search_query: str):
        """Получение вакансий при помощи SJAPI"""
        options = {'keyword': search_query, 'count': 100}
        response = requests.get(self.url, headers=self.headers, options=options)
        if response.status_code == 200:
            data = response.json()
            vacancies_data = data['object']
            vacancies = []
            for vacancy in vacancies_data:
                title = vacancy['profession']
                salary = SJAPI.get_salary(vacancy)
                description = vacancy['candidat']
                url = vacancy['link']
                vacancy = Vacancy(title, salary, description, url)
                vacancies.append(vacancy)
            return vacancies
        else:
            return f'Error: {response.status_code}'
