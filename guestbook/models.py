from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return self.comment
