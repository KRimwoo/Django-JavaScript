from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment,ArticleImage

# Create your views here.

def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.author = request.user
        article.save()
        for img in request.FILES.getlist('image'):
            article_image = ArticleImage()
            article_image.article = article
            article_image.image = img
            article_image.save()
        # article.save()
        return redirect('article:detail', id = article.id)

    return render(request, 'new.html')

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    images = article.images.all()
    comments = article.comments.all()
    like_count = article.total_like()

    return render(request, 'detail.html', {'article': article, 'comments': comments,'images':images,'like_count':like_count})


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        for img in article.images.all():
            img.delete()
        for img in request.FILES.getlist('image'):
            article_image = ArticleImage()
            article_image.article = article
            article_image.image = img
            article_image.save()
        return redirect('article:detail', id=article.id)

    return render(request, 'edit.html', {'article':article})


def destroy(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    return redirect('main:index')

def post_comment(request, id):
    comment=Comment()
    comment.content = request.POST.get('content')
    comment.article = get_object_or_404(Article, pk=id)
    comment.author = request.user
    comment.save()
    return redirect('article:detail', id = id)

def destroy_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return redirect('article:detail', id = id)

def post_like(request, id):
    if request.user.is_anonymous:
        return redirect('user:signin')

    else:
        article = get_object_or_404(Article, pk=id)
        like=article.like.filter(user=request.user)
        if like:
            like.remove(request.user)
            return redirect('article:detail', id)
        else:
            like.article = get_object_or_404(Article, pk=id)
            like.like.add(request.user) 
            return redirect('article:detail', id)
 
