from django.db import models

# Create your models here.

from django.utils import timezone



class Comment (models.Model):
    channel = models.TextField(null=True)
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    #article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    def publish(self):
        self.published_at = timezone.now()
        self.save() 

    def __str__(self):
        return self.text