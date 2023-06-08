from django.contrib import admin
from .models import Car
from django.contrib.admin import ModelAdmin
# Register your models here.

class CarAdmin(ModelAdmin):
    pass

admin.site.register(Car,CarAdmin)