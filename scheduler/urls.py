from django.urls import path,re_path
from scheduler import restfulapi

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apitest/', views.api_tester),
    path('projects/', restfulapi.ProjectsList.as_view()),
    path('projects/<project_id>/', restfulapi.ProjectDetail.as_view()),
    path('events/', restfulapi.EventsList.as_view()),
    path('events/<event_id>/', restfulapi.EventDetail.as_view()),
    # path('comments/', restfulapi.CommentsList.as_view()),
    # path('comments/<commentt_id>/', restfulapi.CommentDetail.as_view())
]