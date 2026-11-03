from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads

# Create your views here.
class Company_list(View):
    def get(self,request):
        company={
            "name":"tcs",
            "location":"banglore",
            "phone":"987654332",
            "email":"tcs@gmail.com"
        }
        return JsonResponse(company)

class JobSeekers_list(View):
    def get(self,request):
        person={
            "name":"Anjali",
            "qualification":"btech cse",
            "contact":"6387436732",
            "email":"anjali@gmail.com",
            "job_role":"software_developer",
            "skills":"python,sql,html,css",
            "experiance":0
        }
        return JsonResponse(person)

class Jobs_list(View):
    def get(self,request):
        job={
            "company":"tcs",
            "job_role":"software engineer trainee",
            "skills":"c,c++,python,sql",
            "salary":"15000",
            "experiance":0,
            "last_date":"2026-06-06"
        }
        return JsonResponse(job)

@method_decorator(csrf_exempt,name='dispatch')
class Applications(View):
    def post(self,request):
        form_data=loads(request.body)
        applicant_name=form_data.get("applicant")
        job_role=form_data.get('job_role')
        applied_on=form_data.get('created_at')
        return JsonResponse({"mesage":f"hello {applicant_name} your application sent to the company"})