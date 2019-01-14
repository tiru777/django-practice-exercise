
from django.urls import path
from . import views

urlpatterns = [

    path('',views.homepage.as_view(), name='home'),
    path('about/',views.aboutpage.as_view(), name='about'),
    path('contactus/',views.contactuspage.as_view(), name='contactus'),
]
