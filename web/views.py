from django.shortcuts import render
from .models import MainPageInfo
from .models import Demand
from .models import Navigation
from .models import Geography
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
    context_skills = {'navigation_results_skills': navigation_results_skills}
    return render(request, 'skills.html', context_skills)

def last_vacancies(request):
    navigation_results_last_vacancies = Navigation.objects.all();
    context_last_vacancies= {'navigation_results_last_vacancies': navigation_results_last_vacancies}
    return render(request, 'last_vacancies.html', context_last_vacancies)