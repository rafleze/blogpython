from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    publish = models.BooleanField(default=False)
    data_pubblicazione = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        ordering = ("-data_pubblicazione",)