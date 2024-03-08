from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=False)
    last_name = models.CharField(max_length=155, null=True, blank=False)


    def __str__(self):
        return self.user.username
    


class Task(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True, blank=False)
    completed = models.BooleanField(default=False, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
