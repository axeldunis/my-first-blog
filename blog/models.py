from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Show(models.Model):
    title=models.CharField(max_length=100)
    platform=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    score_audience=models.CharField(max_length=100)
    score_critic=models.CharField(max_length=100)
    img=models.CharField(max_length=200)

    def __str__(self):
        return self.title

    
    