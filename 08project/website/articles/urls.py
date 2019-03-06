
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='detailview'),

]
