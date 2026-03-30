from django.contrib import admin
from .models import Flat, Maintenance_Notes, Cleaner

# Register your models here.
admin.site.register(Flat)
admin.site.register(Maintenance_Notes)
admin.site.register(Cleaner)