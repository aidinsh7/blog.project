from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    intro = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField()
    slug = models.SlugField()
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

