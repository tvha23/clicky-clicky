from django.urls import path

from api.views import company_list, vacancy_list, company_details, vacancy_details, top_10_vacancies, vacancies_by_company

urlpatterns = [
    path('companies/', company_list ),
    path('companies/<int:id>', company_details ),
    path('companies/<int:id>/vacancies', vacancies_by_company),
    path('vacancies/', vacancy_list ),
    path('vacancies/<int:id>', vacancy_details ),
    path('vacancies/top_ten', top_10_vacancies ),

]
