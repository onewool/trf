from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'traffico'

urlpatterns = [

    # base_views.py
    path('', base_views.index, name='index'),
    path('introduce', base_views.introduce, name='introduce'),
    path('board', base_views.board, name='board'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('gyeonggi/', base_views.gyeonggi, name='gyeonggi'),
    path('seoul/', base_views.seoul, name='seoul'),
    path('gangwon/', base_views.gangwon, name='gangwon'),
    path('chungcheong/', base_views.chungcheong, name='chungcheong'),
    path('gyeongsang/', base_views.gyeongsang, name='gyeongsang'),
    path('jeolla/', base_views.jeolla, name='jeolla'),
    path('sitemap/', base_views.sitemap, name='sitemap'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),



]
