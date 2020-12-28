from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('news', views.news),
    path('tickets', views.tickets),
]
