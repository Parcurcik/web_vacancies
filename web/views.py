from django.shortcuts import render
from .models import MainPageInfo

def home(request):
    query_results = MainPageInfo.objects.all();

    # Creating a dictionary to pass as an argument
    context = {'query_results': query_results}
    return render(request, 'index.html', context)

def demand(request):
    return render(request, 'demand.html')

def geography(request):
    return render(request, 'geography.html')

def skills(request):
    return render(request, 'skills.html')

def last_vacancies(request):
    return render(request, 'last_vacancies.html')