from django.urls import path
from . import views

app_name= 'board'
urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
    path('thread/<int:pk>', views.thread_comment_list, name='thread_comment_list'),
    path('thread/create', views.thread_create, name='thread_create'),
    path('thread/<int:pk>/comment/create', views.thread_comment_create, name='thread_comment_create'),
]