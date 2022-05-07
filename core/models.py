from msilib.schema import Class
from django.db import models

class Employers(models.Model):
    class Meta:
        verbose_name = 'Employer' 
        verbose_name_plural =  'Employers'
    
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    job = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.first_name
