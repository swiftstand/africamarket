from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.conf import settings
from PIL import Image
# Create your models here.



CATEGORY_CHOICES= (
                ('None', 'None'),
                ('Electronics', 'Electronics'),
                ('Arts and Crafts', 'Arts and Crafts'),
                ('Native Attires', 'Native Attires'),
                ('Foreign Attire', 'Foreign Attire'),
                ('Indigenous Fashion Accesssories', 'Indigenous Fashion Accesssories'),
                ('Foreign Fashion Accesssories', 'Foreign Fashion Accesssories'),
                ('Make-ups', 'Make-ups'),
                ('Agricultural Produce', 'Agricultural Produce'),
                ('Building Materials', 'Building Materials'),
                ('Vehicles', 'Vehicles'),
                ('Cosmetics', 'Cosmetics'),
                ('Services', 'Services'),
                ('Bookstores', 'Bookstores'),
                ('Automobiles', 'Automobiles'),
                ('Interiors', 'Interiors'),
                ('Hardware Store','Hardware Store'),
                ('Hotels', 'Hotels'),
                ('Cooking Utensils', 'Cooking Utensils')

             )


STARS_RATINGS= (('Novice','Novice'),
                ('Amateur','Amateur'),
                ('Senior', 'Senior'),
                ('Proffessional', 'Proffessional'),
                ('Veteran','Veteran'),
                ('Master', 'Master'),
                ('Ultimate', 'Ultimate'),
                ('Emerald','Emerald'),
                ('Sapphire', 'Sapphire'),
                ('Gold', 'Gold'),
                ('Diamond','Diamond'),
                ('Warrior', 'Warrior'),
                ('AfricaKing','Africa King')

)

BUYER_PAYMENT_OPTION=(('POD','Buyer Pays On Point Of Delivery Only'),
                    ('AMP', 'Buyer pays through our Admins with AfricaMarket simba only(buyer can be refunded if transaction is not fufilled)'),
                    ('BTH','Payment on Delivery And through our Admins with AfricaMarket simba(buyer can be refunded if transaction is not fufilled)'))




class User(AbstractUser):
    is_seller = models.BooleanField('is a seller', default=False)
    is_buyer = models.BooleanField('is a buyer', default=False)
    store_name=models.CharField(null=True, max_length=100, unique=True)
    base_country = CountryField(blank_label='(select country)')
    city = models.CharField(default='None', max_length=100)
    mobile_number=models.IntegerField(null=True,unique=True)
    image= models.ImageField(default='user_default.jpg', upload_to='user_profile_pics')
    address= models.CharField(max_length=500,null=True)
    address2= models.CharField(max_length=500,null=True)
    ams_worth= models.DecimalField('ams',default=0,max_digits=12,decimal_places=2)

    def save(self,*args, **kwargs):
        super().save()
        if self.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)

            if img.height < 200 or img.width < 200:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)


        super(User,self).save(*args, **kwargs)



    def __str__(self):
            return self.username



class SellerProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    operating_countries=CountryField(blank_label='(select country)',multiple=True, blank=True)
    account_status=models.CharField(default='free', max_length=7)
    about_store=models.TextField('store-bio',blank=True,max_length=350,default='optional')
    is_free = models.BooleanField('Account is free', default=True)
    is_premium = models.BooleanField('Account is premium', default=False)
    is_diamond = models.BooleanField('Account is Diamond', default=False)
    store_payment_method=models.CharField(choices=BUYER_PAYMENT_OPTION,default='BTH',max_length=200)

    def __str__(self):
        if self.is_free==True:
            return '{} sellerprofile and account is free'.format(self.user.username)

        elif self.is_premium==True:
            return '{} sellerprofile and account is premium'.format(self.user.username)
        else:
            return '{} sellerprofile and account is diamond'.format(self.user.username)



class AdminProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alias=models.CharField(null=True, max_length =100, unique=True)
    operating_countries=CountryField(blank_label='(select country)',multiple=True)


    def __str__(self):
            return '{} Adminprofile'.format(self.user.username)


class BuyerProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders=models.TextField(blank=True)

    def __str__(self):
        return '{} Buyerprofile'.format(self.user.username)

class ShelfFlags(models.Model):
    flags_owner=models.OneToOneField(SellerProfile,on_delete=models.CASCADE)
    pre = models.BooleanField(default=False)
    dia = models.BooleanField(default=False)


    def __str__(self):
        return'flags of seller {}'.format(self.flags_owner.user.username)

