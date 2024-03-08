from django.contrib import admin
from todo import models

# Register your models here.


admin.site.register(models.Profile)
admin.site.register(models.Task)