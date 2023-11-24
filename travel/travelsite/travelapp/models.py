from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='photos')
    dec = models.TextField()
    def __str__(self):
        return self.name
class founder(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='photos')
    dec = models.TextField()
    def __str__(self):
        return self.name
