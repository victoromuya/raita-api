from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    
    def __str__(self):
        return self.title
    
    
    title = models.CharField(default="title", max_length=20)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    userid = models.CharField(default="username", max_length=20)
    date = models.CharField(default="today", max_length=100)
    
    
# class Comments(models.Model):
    
#     def __str__(self):
#         return self.articleid
    
    
#     articleid = models.IntegerField(default=34)
#     userid = models.CharField(default="today", max_length=50)
#     description = models.TextField()
#     date = models.CharField(default="today", max_length=100)

class Commenting(models.Model):
    
    def __str__(self):
            return (str(self.article_id) + "__" + self.userid)
    
    article_id = models.IntegerField(default=0)
    userid = models.CharField(default="today", max_length=50)
    comments = models.TextField(default="enter comment")
    date = models.CharField(default="today", max_length=100)