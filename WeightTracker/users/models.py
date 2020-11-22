from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
