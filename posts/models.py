from django.db import models
# from PIL import Image
# Create your models here.
from django.urls import reverse
from ckeditor.fields import RichTextField



class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,upload_to='images')

    def __str__(self):
        return self.title

    # def save(self,*args, **kwargs):
    #     super(Post, self).save(*args,**kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 200 or img.width > 200 :
    #         new_size = (200,200)
    #         img.thumbnail(new_size)
    #         img.save(self.image.path)


    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})

