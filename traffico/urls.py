from django.urls import path

from . import views

app_name = 'traffico'

urlpatterns = [
    path('', views.index, name='index'),
    path('board', views.board, name='board'),
    path('introduce', views.introduce, name='introduce'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]