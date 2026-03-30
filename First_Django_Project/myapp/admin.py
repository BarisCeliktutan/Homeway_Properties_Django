from django.contrib import admin
from .models import ToDoList, Users, ButcherNBlackbird

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Users)
admin.site.register(ButcherNBlackbird)



# You need to run this on terminal every time you make a change to any of your database models.
# python manage.py makemigrations
# Then this to update the database.
# python manage.py migrate

# User following command to create a user:
# python manage.py createsuperuser

# superuser details:
# username baris
# email => blank
# password 1asiasa1

# 1asiasa1
# AsiasASoftwareEngineer
# This wasn't a superuser, I made it a superuser by doing this:
# python manage.py shell
# from django.contrib.auth import User
# user = User.objects.get(username="1asiasa1")
# user.is_superuser = True
# user.is_staff = True
# user.save()
