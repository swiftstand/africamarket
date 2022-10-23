from django.db import models
from django.conf import settings
from PIL import Image
from users.models import SellerProfile
import itertools
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
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

STATUS=(('new','new'),
        ('best-seller','best-seller'),
        ('top-featured','top-featured')
        )





class ShelfOne(models.Model):
    shelf_owner=models.OneToOneField(SellerProfile,on_delete=models.CASCADE)
    shelf_name=models.CharField(max_length=20, blank=False)
    image = models.ImageField(default='shelf_default.jpg', upload_to='shelf_profile_pics')
    shelf_category=models.CharField(choices=CATEGORY_CHOICES,default='NONE',max_length=50)
    shelf_size=models.IntegerField(default=50,editable=False)
    slug=models.SlugField(default='',editable=False,max_length=1000)


    def _generate_slug(self):
        max_length=self._meta.get_field('slug').max_length
        if self.shelf_owner.user.store_name is not None:
            joint_value='seller '+self.shelf_owner.user.username+' store '+self.shelf_owner.user.store_name+' based in '+self.shelf_owner.user.base_country.name+'F shelf'
        else:
            joint_value='seller  '+self.shelf_owner.user.username+self.shelf_owner.user.base_country.name+'F shelf'
        value=joint_value
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if slug_candidate not in ShelfFive.objects.filter(slug=slug_candidate):
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate


    def save(self,*args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save()
        if self.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)

            elif img.height < 200 or img.width < 200:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)



    def __str__(self):
        return 'All free shelf {} owned by {} and managed by user {}'.format(self.shelf_name, self.shelf_owner.user.store_name, self.shelf_owner.user.username)



class ShelfTwo(models.Model):
    shelf_owner=models.OneToOneField(SellerProfile,on_delete=models.CASCADE)
    shelf_name=models.CharField(max_length=20, blank=False)
    image = models.ImageField(default='shelf_default.jpg', upload_to='shelf_profile_pics')
    shelf_category=models.CharField(choices=CATEGORY_CHOICES,default='NONE',max_length=50)
    shelf_size=models.IntegerField(default=75,editable=False)
    slug=models.SlugField(default='',editable=False,max_length=1000)

    def _generate_slug(self):
        max_length=self._meta.get_field('slug').max_length
        if self.shelf_owner.user.store_name is not None:
            joint_value='seller '+self.shelf_owner.user.username+' store '+self.shelf_owner.user.store_name+' based in '+self.shelf_owner.user.base_country.name+'P shelf'
        else:
            joint_value='seller '+self.shelf_owner.user.username+self.shelf_owner.user.base_country.name+'P1 shelf'
        value=joint_value
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if slug_candidate not in ShelfTwo.objects.filter(slug=slug_candidate):
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self,*args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save()
        if self.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 200 or img.width < 200:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)


    def __str__(self):
        return 'Premium And Diamond {} owned by {} and managed by user {}'.format(self.shelf_name, self.shelf_owner.user.store_name, self.shelf_owner.user.username)

class ShelfThree(models.Model):
    shelf_owner=models.OneToOneField(SellerProfile,on_delete=models.CASCADE)
    shelf_name=models.CharField(max_length=20, blank=False)
    image = models.ImageField(default='shelf_default.jpg', upload_to='shelf_profile_pics')
    shelf_category=models.CharField(choices=CATEGORY_CHOICES,default='NONE',max_length=50)
    shelf_size=models.IntegerField(default=75,editable=False)
    slug=models.SlugField(default='',editable=False,max_length=1000)


    def _generate_slug(self):
        max_length=self._meta.get_field('slug').max_length
        if self.shelf_owner.user.store_name is not None:
            joint_value='seller '+self.shelf_owner.user.username+' store '+self.shelf_owner.user.store_name+' based in '+self.shelf_owner.user.base_country.name+'P2 shelf'
        else:
            joint_value='seller '+self.shelf_owner.user.username+self.shelf_owner.user.base_country.name+'P2 shelf'
        value=joint_value
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if slug_candidate not in ShelfThree.objects.filter(slug=slug_candidate):
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self,*args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save()
        if self.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 200 or img.width < 200:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)


    def __str__(self):
        return 'Premium And Diamond shelf {} owned by {} and managed by user {}'.format(self.shelf_name, self.shelf_owner.user.store_name, self.shelf_owner.user.username)

class ShelfFour(models.Model):
    shelf_owner=models.OneToOneField(SellerProfile,on_delete=models.CASCADE)
    shelf_name=models.CharField(max_length=20, blank=False)
    image = models.ImageField(default='shelf_default.jpg', upload_to='shelf_profile_pics')
    shelf_category=models.CharField(choices=CATEGORY_CHOICES,default='NONE',max_length=50)
    shelf_size=models.IntegerField(default=100,editable=False)
    slug=models.SlugField(default='',editable=False,max_length=1000)


    def _generate_slug(self):
        max_length=self._meta.get_field('slug').max_length
        if self.shelf_owner.user.store_name is not None:
            joint_value='seller '+self.shelf_owner.user.username+' store '+self.shelf_owner.user.store_name+' based in '+self.shelf_owner.user.base_country.name+'D1 shelf'
        else:
            joint_value='seller '+self.shelf_owner.user.username+self.shelf_owner.user.base_country.name+'D1 shelf'
        value=joint_value
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if slug_candidate not in ShelfFour.objects.filter(slug=slug_candidate):
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self,*args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save()
        if self.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 200 or img.width < 200:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)



    def __str__(self):
        return 'Diamond shelf {} owned by {} and managed by user {}'.format(self.shelf_name, self.shelf_owner.user.store_name, self.shelf_owner.user.username)

class ShelfFive(models.Model):
    shelf_owner=models.OneToOneField(SellerProfile,on_delete=models.CASCADE)
    shelf_name=models.CharField(max_length=20, blank=False,)
    image = models.ImageField(default='shelf_default.jpg', upload_to='shelf_profile_pics')
    shelf_category=models.CharField(choices=CATEGORY_CHOICES,default='NONE',max_length=50)
    shelf_size=models.IntegerField(default=1000)
    slug=models.SlugField(default='',editable=False,max_length=1000)


    def _generate_slug(self):
        max_length=self._meta.get_field('slug').max_length
        if self.shelf_owner.user.store_name is not None:
            joint_value='seller '+self.shelf_owner.user.username+' store '+self.shelf_owner.user.store_name+' based in '+self.shelf_owner.user.base_country.name+'D2 shelf'
        else:
            joint_value='seller '+self.shelf_owner.user.username+self.shelf_owner.user.base_country.name+'D2 shelf'
        value=joint_value
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if slug_candidate not in ShelfFive.objects.filter(slug=slug_candidate):
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self,*args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save()
        if self.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 200 or img.width < 200:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)


    def __str__(self):
        return 'Diamond shelf {} owned by {} and managed by user {}'.format(self.shelf_name, self.shelf_owner.user.store_name, self.shelf_owner.user.username)


class ItemShelfOne(models.Model):
    shelf=models.ForeignKey(ShelfOne, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to='item_pics')
    name=models.CharField(max_length=100, default='nameless',blank=False)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    discount_price=models.DecimalField(max_digits=12,decimal_places=2,blank=True,default=0)
    item_description=models.TextField(max_length=250,blank=True,null=True)
    status=models.CharField(choices=STATUS,max_length=15)
    multiplier=models.DecimalField(max_digits=3,decimal_places=2,default=0.50,editable=False)
    ams_value=models.DecimalField(max_digits=1000,decimal_places=2,null=False,editable=False)
    date_posted= models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('itemsone', kwargs={'store_name':self.shelf.shelf_owner.user.store_name,'pk':self.shelf.pk,'slug':self.shelf.slug})


    def convert(self):
        m=float(self.multiplier)
        n=float(self.price)
        e=float(self.discount_price)
        f=n-e
        p=m*f
        self.ams_value=float(p)


    def save(self,*args, **kwargs):
        self.convert()
        super().save()
        if self.pk<=self.shelf.shelf_size:
            if self.shelf.shelf_owner.user.is_authenticated:
                img = Image.open(self.image.path)
                if img.height > 300 or img.width > 380:
                    output_size = (420,500)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
                elif img.height < 300 or img.width < 380:
                    output_size = (420,500)
                    img.thumbnail(output_size)
                    img.save(self.image.path)


    def __str__(self):
        return '{} in free_shelf {} and is owned by user {}'.format(self.name, self.shelf.shelf_name, self.shelf.shelf_owner.user.username)


class ItemShelfTwo(models.Model):
    shelf=models.ForeignKey(ShelfTwo, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to='item_pics')
    name=models.CharField(max_length=100, default='nameless',blank=False)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    discount_price=models.DecimalField(max_digits=12,decimal_places=2,blank=True,default=0)
    item_description=models.TextField(max_length=250,blank=True,null=True)
    status=models.CharField(choices=STATUS,max_length=15)
    multiplier=models.DecimalField(max_digits=3,decimal_places=2,default=0.50,editable=False)
    ams_value=models.DecimalField(max_digits=1000,decimal_places=2,null=False,editable=False)
    date_posted= models.DateField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('itemstwo', kwargs={'store_name':self.shelf.shelf_owner.user.store_name,'pk':self.shelf.pk,'slug':self.shelf.slug})

    def convert(self):
        m=float(self.multiplier)
        n=float(self.price)
        e=float(self.discount_price)
        f=n-e
        p=m*f
        self.ams_value=float(p)

    def save(self,*args, **kwargs):
        self.convert()
        super().save()
        if self.shelf.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 300 or img.width < 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)


    def __str__(self):
        return '{} in Premium_shelf {} and is owned by user {}'.format(self.name, self.shelf.shelf_name, self.shelf.shelf_owner.user.username)

class ItemShelfThree(models.Model):
    shelf=models.ForeignKey(ShelfThree, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to='item_pics')
    name=models.CharField(max_length=100, default='nameless',blank=False)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    discount_price=models.DecimalField(max_digits=12,decimal_places=2,blank=True,default=0)
    item_description=models.TextField(max_length=250,blank=True,null=True)
    status=models.CharField(choices=STATUS,max_length=15)
    multiplier=models.DecimalField(max_digits=3,decimal_places=2,default=0.50,editable=False)
    ams_value=models.DecimalField(max_digits=1000,decimal_places=2,null=False,editable=False)
    date_posted= models.DateField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('itemsthree', kwargs={'store_name':self.shelf.shelf_owner.user.store_name,'pk':self.shelf.pk,'slug':self.shelf.slug})


    def convert(self):
        m=float(self.multiplier)
        n=float(self.price)
        e=float(self.discount_price)
        f=n-e
        p=m*f
        self.ams_value=float(p)

    def save(self,*args, **kwargs):
        self.convert()
        super().save()
        if self.shelf.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 300 or img.width < 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)



    def __str__(self):
        return '{} in Premium_shelf {} and is owned by user {}'.format(self.name, self.shelf.shelf_name, self.shelf.shelf_owner.user.username)

class ItemShelfFour(models.Model):
    shelf=models.ForeignKey(ShelfFour, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to='item_pics')
    name=models.CharField(max_length=100, default='nameless',blank=False)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    dicount_price=models.DecimalField(max_digits=12,decimal_places=2,blank=True,default=0)
    item_description=models.TextField(max_length=250,blank=True,null=True)
    status=models.CharField(choices=STATUS,max_length=15)
    multiplier=models.DecimalField(max_digits=3,decimal_places=2,default=0.50,editable=False)
    ams_value=models.DecimalField(max_digits=1000,decimal_places=2,null=False,editable=False)
    date_posted= models.DateField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('itemsfour', kwargs={'store_name':self.shelf.shelf_owner.user.store_name,'pk':self.shelf.pk,'slug':self.shelf.slug})

    def convert(self):
        m=float(self.multiplier)
        n=float(self.price)
        e=float(self.discount_price)
        f=n-e
        p=m*f
        self.ams_value=float(p)


    def save(self,*args, **kwargs):
        self.convert()
        super().save()
        if self.shelf.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 300 or img.width < 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return '{} in Premium_shelf {} and is owned by user {}'.format(self.name, self.shelf.shelf_name, self.shelf.shelf_owner.user.username)

class ItemShelfFive(models.Model):
    shelf=models.ForeignKey(ShelfFive, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to='item_pics')
    name=models.CharField(max_length=100, default='nameless',blank=False)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    discount_price=models.DecimalField(max_digits=12,decimal_places=2,blank=True,default=0)
    item_description=models.TextField(max_length=250,blank=True,null=True)
    status=models.CharField(choices=STATUS,max_length=15)
    multiplier=models.DecimalField(max_digits=3,decimal_places=2,default=0.50,editable=False)
    ams_value=models.DecimalField(max_digits=1000,decimal_places=2,null=False,editable=False)
    date_posted= models.DateField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('itemsfive', kwargs={'store_name':self.shelf.shelf_owner.user.store_name,'pk':self.shelf.pk,'slug':self.shelf.slug})

    def convert(self):
        m=float(self.multiplier)
        n=float(self.price)
        e=float(self.discount_price)
        f=n-e
        p=m*f
        self.ams_value=float(p)


    def save(self,*args, **kwargs):
        self.convert()
        super().save()
        if self.shelf.shelf_owner.user.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)
            elif img.height < 300 or img.width < 380:
                output_size = (420,500)
                img.thumbnail(output_size)
                img.save(self.image.path)


    def __str__(self):
        return '{} in Premium_shelf {} and is owned by user {}'.format(self.name, self.shelf.shelf_name, self.shelf.shelf_owner.user.username)


