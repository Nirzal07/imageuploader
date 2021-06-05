from django.db import models
from django.contrib.auth.models import User

class Images(models.Model):
    photo = models.ImageField(upload_to='images')
    upload_time = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
