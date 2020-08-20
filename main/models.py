from django.db import models
from django.urls import reverse
from .services import get_image_from_url
from django.core.files import File


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    url = models.URLField(unique=False, blank=True)
    update_image = models.ImageField(upload_to='images/update', blank=True)
    description = models.CharField(max_length=256, blank=True)

    def get_absolute_url(self):
        return reverse('main:image_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.url and not self.image:
            content = get_image_from_url(self.url)
            self.image.save(f"image.jpeg", File(content))
        super(Image, self).save(*args, **kwargs)