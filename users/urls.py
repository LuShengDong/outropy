from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up/api', views.sign_up_api, name='sign_up_api'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_in/api', views.sign_in_api, name='sign_in_api'),

]