from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:news_id>', views.views_news, name='view_news'),
]