from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class UpdateOnlyManager(models.Manager):
    
    def create(self, *args, **kwargs):
        # Melarang operasi create() dengan raising exception
        raise NotImplementedError("You cannot use create() with this manager.")

    def bulk_create(self, *args, **kwargs):
        # Melarang operasi bulk_create() dengan raising exception
        raise NotImplementedError("You cannot use bulk_create() with this manager.")


class aboutus(models.Model):
    title = models.TextField()

    def __str__(self) :
        return self.title


class sliders(models.Model):
    titleImage = models.CharField(max_length=256)
    image = models.ImageField(upload_to='static/img')
    descImage = models.TextField()
    # colorBackground = ColorField(verbose_name='color', default='#FFFFFF')
    colorBackground = ColorField(image_field="image")

    readonly_fields = {colorBackground}

    def __str__(self) :
        return self.titleImage
