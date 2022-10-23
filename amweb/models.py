from django.db import models
from django.utils import timezone
from django.conf import settings
from PIL import Image
from django.urls import reverse
import itertools
from django.utils.text import slugify
# Create your models here.


class AdminPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    content = models.TextField()
    image= models.ImageField(default='post_defaults.jpg', upload_to='Adminpost_pics')
    date_posted= models.DateField(default=timezone.now)
    summary=models.TextField(max_length=300,blank=True)
    slug=models.SlugField(default='',editable=False,max_length=1000)


    def _generate_slug(self):
        max_length=self._meta.get_field('slug').max_length
        value='by '+ self.author.adminprofile.alias+ ' title '+self.title+str(len(self.content))
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if slug_candidate not in AdminPost.objects.filter(slug=slug_candidate):
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate



    def save(self,*args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save()
        if self.author.is_authenticated:
            img = Image.open(self.image.path)
            if img.height > 550 or img.width > 650:
                output_size = (650,550)
                img.thumbnail(output_size)
                img.save(self.image.path)

            if img.height < 433 or img.width < 650:
                output_size = (650,550)
                img.thumbnail(output_size)
                img.save(self.image.path)

        super(AdminPost,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

