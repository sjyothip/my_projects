from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	phone = models.CharField(max_length=224,blank=True,null=True)
	profile_pic = models.ImageField(upload_to='Images',null=True,blank=True)
	
class Messages(models.Model):
	msgs = models.CharField(max_length=224,blank=True,null=True)
	added_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	sender_id = models.CharField(max_length=224,blank=True,null=True)
	shared_files = models.FileField(upload_to='File',null=True,blank=True)

class Testdates(models.Model):
	added_at = models.DateTimeField(auto_now_add=True)
	added_now = models.DateTimeField(auto_now=True)
