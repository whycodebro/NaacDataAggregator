from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Alluser(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    user_type= models.CharField(max_length=30)
    mobile=models.CharField(max_length=10,null=True,blank=True,default=None)
    def __str__(self):
        return (str(self.user) +'@'+self.user_type)