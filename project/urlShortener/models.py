from django.db import models
from .utils import create_shortened_url
class Shortener(models.Model):
    originalURL = models.URLField()
    newURL = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return f'{self.originalURL} to {self.newURL}'

    def save(self, *args, **kwargs):   #(kwargs allows you to pass keyworded variable length of arguments to a function) 
        if not self.newURL:
            self.newURL = create_shortened_url(self)
        super().save(*args, **kwargs)