
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='detailview'),
    path('detail/create/',views.BlogCreateView.as_view(), name='create_blog'),
    path('detail/<int:pk>/update/',views.BlogUpdateView.as_view(),name='update_blog'),
    path('detail/<int:pk>/delete/',views.BlogDeleteView.as_view(),name='delete_blog'),

]
