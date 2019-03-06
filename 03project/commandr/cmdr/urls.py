
from django.urls import path
from cmdr import views

urlpatterns = [
    path('',views.loginpageview.as_view(), name="login"),
]
