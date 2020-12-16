from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, help_text='title')
    message = models.CharField(max_length=120, help_text="write message")
    def __str__(self):
        return self.title + self.message