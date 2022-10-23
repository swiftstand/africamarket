#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sulaiman maryam
#
# Created:     30-05-2020
# Copyright:   (c) sulaiman maryam 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from django.db.models.signals import post_save,pre_init,post_init
from .models import User,AdminProfile,BuyerProfile,SellerProfile,ShelfFlags
from inventory.models import ShelfOne,ShelfTwo,ShelfThree,ShelfFour,ShelfFive
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=User)
def create_adminprofile(sender, instance, created, **kwargs):
    if instance.is_staff==True or instance.is_superuser==True:
        if created:
            AdminProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_adminprofile(sender, instance, **kwargs):
    if instance.is_staff==True or instance.is_superuser==True:
        instance.adminprofile.save()



@receiver(post_save, sender=User)
def create_sellerprofile(sender, instance, created, **kwargs):
    if instance.is_seller==True :
        if created:
            SellerProfile.objects.create(user=instance)

    if instance.is_superuser==True:
        if created:
            SellerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_sellerprofile(sender, instance, **kwargs):
    if instance.is_seller==True:
        instance.sellerprofile.save()

    if instance.is_superuser==True:
        instance.sellerprofile.save()



@receiver(post_save, sender=User)
def create_buyerprofile(sender, instance, created, **kwargs):
    if instance.is_buyer==True :
        if created:
            BuyerProfile.objects.create(user=instance)
    if instance.is_superuser==True:
        if created:
            BuyerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_buyerprofile(sender, instance, **kwargs):
    if instance.is_buyer==True:
        instance.buyerprofile.save()
    if instance.is_superuser==True:
        instance.buyerprofile.save()



@receiver(post_save, sender=SellerProfile)
def create_shelfone(sender, instance, created, **kwargs):
    if instance.user.is_seller==True :
        if created:
            ShelfOne.objects.create(shelf_owner=instance)
    if instance.user.is_superuser==True:
        if created:
            ShelfOne.objects.create(shelf_owner=instance)

@receiver(post_save, sender=SellerProfile)
def save_shelfone(sender, instance, **kwargs):
    if instance.user.is_seller==True:
        instance.shelfone.save()
    if instance.user.is_superuser==True:
        instance.shelfone.save()


@receiver(post_save, sender=SellerProfile)
def create_shelfflags(sender,instance,created,**kwargs):
    if instance.user.is_seller==True:
        if created:
            ShelfFlags.objects.create(flags_owner=instance)
    if instance.user.is_superuser==True:
        if created:
            ShelfFlags.objects.create(flags_owner=instance)


@receiver(post_save, sender=SellerProfile)
def save_shelfflags(sender, instance, **kwargs):
    if instance.user.is_seller==True:
        instance.shelfflags.save()
    if instance.user.is_superuser==True:
        instance.shelfflags.save()

@receiver(post_save, sender=SellerProfile)
def create_shelftwo(sender, instance, created, **kwargs):
    flag=get_object_or_404(ShelfFlags,flags_owner=instance)
    print('i am preeeeee',flag)
    if instance.shelfflags.pre==False:
        if instance.user.is_seller==True and instance.is_free==False:
            if not created:
                ShelfTwo.objects.create(shelf_owner=instance)
        if instance.user.is_superuser==True:
            if created:
                ShelfTwo.objects.create(shelf_owner=instance)

@receiver(post_save, sender=SellerProfile)
def save_shelftwo(sender, instance, **kwargs):
    if instance.user.is_seller==True and instance.is_free==False:
        instance.shelftwo.save()
    if instance.user.is_superuser==True:
        instance.shelftwo.save()



@receiver(post_save, sender=SellerProfile)
def create_shelfthree(sender, instance, created, **kwargs):
    if instance.shelfflags.pre==False:
        if instance.user.is_seller==True and instance.is_free==False:
            if not created:
                ShelfThree.objects.create(shelf_owner=instance)
                flag=ShelfFlags.objects.get(flags_owner=instance)
                flag.pre=True
                flag.save(update_fields=['pre'])
        if instance.user.is_superuser==True:
            if created:
                ShelfThree.objects.create(shelf_owner=instance)
                flag=ShelfFlags.objects.get(flags_owner=instance)
                flag.pre=True
                flag.save(update_fields=['pre'])
                print(flag.pre)

@receiver(post_save, sender=SellerProfile)
def save_shelfthree(sender, instance, **kwargs):
    if instance.user.is_seller==True and instance.is_free==False:
        instance.shelfthree.save()
    if instance.user.is_superuser==True:
        instance.shelfthree.save()



@receiver(post_save, sender=SellerProfile)
def create_shelffour(sender, instance, created, **kwargs):
    if instance.shelfflags.dia==False:
        if instance.user.is_seller==True and instance.is_free==False and instance.is_premium==False and instance.is_diamond==True :
            if not created:
                ShelfFour.objects.create(shelf_owner=instance)
        if instance.user.is_superuser==True:
            if created:
                ShelfFour.objects.create(shelf_owner=instance)

@receiver(post_save, sender=SellerProfile)
def save_shelffour(sender, instance, **kwargs):
    if instance.user.is_seller==True and instance.is_free==False and instance.is_premium==False and instance.is_diamond==True:
        instance.shelffour.save()
    if instance.user.is_superuser==True:
        instance.shelffour.save()


@receiver(post_save, sender=SellerProfile)
def create_shelffive(sender, instance, created, **kwargs):
    if instance.shelfflags.dia==False:
        if instance.user.is_seller==True and instance.is_free==False and instance.is_premium==False and instance.is_diamond==True:
            if not created:
                ShelfFive.objects.create(shelf_owner=instance)
                flag=ShelfFlags.objects.get(flags_owner=instance)
                flag.dia=True
                flag.save(update_fields=['dia'])
        if instance.user.is_superuser==True:
            if created:
                ShelfFive.objects.create(shelf_owner=instance)
                flag=ShelfFlags.objects.get(flags_owner=instance)
                flag.dia=True
                flag.save(update_fields=['dia'])

@receiver(post_save, sender=SellerProfile)
def save_shelffive(sender, instance, **kwargs):
    if instance.user.is_seller==True:
        if instance.is_free==False and instance.is_premium==False and instance.is_diamond==True:
            instance.shelffive.save()
    if instance.user.is_superuser==True:
        instance.shelffive.save()


