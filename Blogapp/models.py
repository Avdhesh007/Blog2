from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    heading=models.CharField(max_length=50)
    blog=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now=True)

