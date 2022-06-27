from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Persons(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    discr=models.TextField()

    def __str__(self):
        return self.name