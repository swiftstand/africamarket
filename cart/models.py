from django.db import models
from users.models import BuyerProfile
# Create your models here.



class Cart(models.Model):
    cart_owner=models.ForeignKey(BuyerProfile,on_delete=models.CASCADE)
