from django.db import models

# Create your models here.
class InfoModel(models.Model):
    name = models.CharField(max_length=120,default='pustuvoncha')
    surname = models.CharField(max_length=120,default='palonchayev')
    date_of_birth = models.DateField(default='2004-10-02')
    gender = models.CharField(max_length=50,default= ' ')
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name 
    
