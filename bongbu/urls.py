from django.urls import path

from .views import base_views, question_views, answer_views, realty_news_views

app_name = 'bongbu'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # path('question/create/', views.question_create, name='question_create'),

    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),

    # realty_news_list.py
    path('realty_news_list', realty_news_views.realty_news_list, name='realty_news_list'),

]