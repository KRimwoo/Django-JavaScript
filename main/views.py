from django.shortcuts import render
from article.models import Article
from django.http import JsonResponse

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def get_articles(request):
    articles = Article.objects.all()
    articles_list = []
    for article in articles:
        articles_list.append(article.to_dict())
    return JsonResponse({"articles":articles_list})