from django.contrib import admin
from django.urls import path
from .views import (index, about, service, job_seeker, contact, 
                    save_contact,vacancy,training,homecare,
                    disability_support,aged_care,find_jobs,job_detail,
                    privacy_policy, time_sheet)
from django.contrib.sitemaps.views import sitemap
from .sitemaps import MySitemap

sitemaps = {
    'mysite': MySitemap,
}

urlpatterns = [
    path('',index,name="index"),
    # path('home',index, name="home"),
    path('about/',about,name="about-us"),
    path('service/',service,name="service"),
    path('homecare/',homecare,name="home-care"),
    path('job-seeker/',job_seeker,name="job-seeker"),
    path('training/',training,name="training"),
    path('disability-support/',disability_support,name="disability-support"),
    path('aged-care/',aged_care,name="aged-care"),
    path('contact/', contact, name = "contact-us"),
    path('save-contact/', save_contact, name="save-contact"),
    path('vacancy/', vacancy, name="vacancy"),
    path('find-jobs/', find_jobs, name="find-jobs"),
    path('job/<int:pk>/', job_detail, name="job-detail"),
    path('privacy-policy/', privacy_policy, name="privacy-policy"),
    path('timesheet/', time_sheet, name="time-sheet"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]