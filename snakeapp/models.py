from django.db import models

# Create your models here.
class Snake(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=128)
    prey = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    venomous = models.CharField(max_length=128)
    
    def save(self, force_insert=False, force_update=False):
        self.name = self.name.title()  
        self.region = self.region.title()  
        super(Snake, self).save(force_insert, force_update)

class Scientist(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
