from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#### When you add/modify a model, you need to run this command "python manage.py makemigrations <app's name>("myapp" in this case)" and then again "python manage.py migrate" on terminal where manage.py stored!

# class TodoItem(models.Model):
#     title = models.CharField(max_length=200)
#     completed = models.BooleanField(default=False)

class Users(models.Model):
    username = models.CharField(max_length=200)

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) ## If you gonna use a model/class that you created, you need to define it by "ForeignKey"
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
class ButcherNBlackbird(models.Model):
    times = models.CharField(max_length=200)
    was_at = models.CharField(max_length=200, default="")
    
    def __str__(self):
        return self.times