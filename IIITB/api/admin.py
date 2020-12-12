from django.contrib import admin
from .models import Branch, Student

# Register your models here.
models_to_register = [Branch, Student]
admin.site.register(models_to_register)