from django.urls import path
from .views import index, get_articles

app_name = 'main'

urlpatterns = [
    path("", index, name='index'),
    path("get_articles", get_articles, name='get_articles'),
]