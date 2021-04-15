from django.shortcuts import render
from django.http.response import JsonResponse

from api.models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies ]
    return JsonResponse(companies_json, safe=False)

def vacancy_list(request):
    vacancies=Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe = False)

def company_details(request, id):   
    try:
        company=Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse( {
            'message':str(e),
            'error': f'Error finding the company with id {id}'
        })
    return JsonResponse(company.to_json())

def vacancy_details(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e :
        return JsonResponse(
            {
                'message':str(e),
                'error':f'Error finding vacancy with id {id}'
            }
        )
    return JsonResponse(vacancy.to_json())

def top_10_vacancies(request):
    vacancies=Vacancy.objects.raw(
        'SELECT * FROM api_vacancy ORDER BY salary DESC LIMIT 10 '
        )
    vacancies_json=[vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancies_by_company(request, id):
    company=Company.objects.get(id=id)
    vacancies = company.vacancy_set
    vacancies_json = [vacancy.to_json() for vacancy in vacancies.all()]
    return JsonResponse(vacancies_json, safe=False)


