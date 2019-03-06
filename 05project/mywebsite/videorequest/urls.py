
from django.urls import path
from videorequest import views

urlpatterns = [

    path('', views.index, name='index'),
    path('vrform/', views.vrform, name='vrform'),
]
