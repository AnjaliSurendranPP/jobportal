from django.urls import path
from . import views

urlpatterns=[
    path('companies/',views.Company_list.as_view(),name='company_list'),
    path('jobseekers/',views.JobSeekers_list.as_view(),name='person_list'),
    path('jobs/',views.Jobs_list.as_view(),name='jobs_list'),
    path('application/',views.Applications.as_view(),name='application')
]