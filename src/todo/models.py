from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist")
    task = models.TextField(max_length=120)
    completed = models.BooleanField(default = False)
    def __str__(self):
        return self.task

