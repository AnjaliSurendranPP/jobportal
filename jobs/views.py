from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def job_list(request):
    data={
        "message":"welcome to jobportal",
        "status":"success"
    }
    return JsonResponse(data)