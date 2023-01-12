from django.shortcuts import render
import requests
import  re
from .models import MainPageInfo
from .models import Demand
from .models import Navigation
from .models import Geography
from .models import Skills
from .models import LastVacancies
def home(request):
    home_results = MainPageInfo.objects.all();
    navigation_results_hone = Navigation.objects.all();
    context_home = {'home_results': home_results, 'navigation_results_hone': navigation_results_hone}
    return render(request, 'index.html', context_home)

def demand(request):
    navigation_results_demand = Navigation.objects.all();
    demand_results = Demand.objects.all();
    context_demand = {'demand_results': demand_results, 'navigation_results_demand': navigation_results_demand}
    return render(request, 'demand.html', context_demand)

def geography(request):
    geography_results = Geography.objects.all();
    navigation_results_geography = Navigation.objects.all();
    context_geography = {'navigation_results_geography': navigation_results_geography,'geography_results': geography_results }
    return render(request, 'geography.html', context_geography)

def skills(request):
    navigation_results_skills = Navigation.objects.all();
    skills_results = Skills.objects.all()
    context_skills = {'navigation_results_skills': navigation_results_skills, 'skills_results': skills_results}
    return render(request, 'skills.html', context_skills)

def last_vacancies(request):
    navigation_results_last_vacancies = Navigation.objects.all();

    class HHAPI:

        def __init__(self, search_text: str):
            self.text = search_text

        def __get_full_vacancies__(self, date: str, count_vac: int) -> list:
            url = 'https://api.hh.ru/vacancies'
            return requests.get(url, dict(text=self.text,
                                          specialization=1,
                                          date_from=f"{date}T00:00:00",
                                          date_to=f"{date}T23:00:00",
                                          per_page=count_vac,
                                          page=1)).json()["items"]

        def get_data_vacancies(self, date: str, count_vac: int):
            data = self.__get_full_vacancies__(date, count_vac)
            result_list = []
            for vac in data:
                url_vac = f'https://api.hh.ru/vacancies/{vac["id"]}'
                resp = requests.get(url_vac).json()
                if resp['salary']:
                    description = ' '.join(re.sub(re.compile('<.*?>'), '', resp['description'])
                                           .strip()
                                           .split())
                    description = description[:2000] + '...' if len(description) >= 2000 else description
                    result_list.append({'name': resp['name'],
                                        'description': description,
                                        'key_skills': list(map(lambda x: x['name'], resp['key_skills'])),
                                        'employer': resp['employer']['name'],
                                        'salary': f"{resp['salary']['from']} - {resp['salary']['to']} {resp['salary']['currency']}",
                                        'area': resp['area']['name'],
                                        'published_at': resp['published_at'][:10],
                                        'alternate_url': resp['alternate_url']})

            return result_list

    hh = HHAPI('Web-разработчик')
    vacs = hh.get_data_vacancies('2022-12-15', 10)



    last_vacancies = LastVacancies.objects.all();

    context_last_vacancies= {'navigation_results_last_vacancies': navigation_results_last_vacancies,
                             'vacs' : vacs, 'last_vacancies': last_vacancies}

    return render(request, 'last_vacancies.html', context_last_vacancies)