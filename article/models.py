from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Article(models.Model):
  author = models.ForeignKey(
    USER,
    on_delete=models.CASCADE,
  )
  title = models.TextField()
  content = models.TextField()

  created_at = models.DateTimeField(
    auto_now_add=True,
  )
  
  updated_at = models.DateTimeField(
    auto_now=True,
  )

  like = models.ManyToManyField(USER, related_name='likes')

  def __str__(self):
    return self.title
  
  def summary(self):
    return self.content[:100]
  
  def total_like(self):
     return self.like.count()
  
  def to_dict(self):
     return {
        'id': self.id,
        'author': self.author.username,
        'title': self.title,
        'content': self.content,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
        'like_count': self.total_like(),
     }

class ArticleImage(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE , related_name='images')
   image = models.ImageField(upload_to='article/')
   

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(USER,on_delete=models.CASCADE, related_name='comments')
