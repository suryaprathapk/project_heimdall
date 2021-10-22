from django.db import models
from datetime import date


# Create your models here.
class Technologies(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(default='NA')
    Link = models.TextField(default='NA')
    Image = models.ImageField(upload_to='images/', default='images/default_software.png')
    manual_EOL_date = models.CharField(max_length=100, default='NA')
    EOL_Approaching = models.CharField(max_length=100, default='NA')
    refresh_date = models.DateField(default=date.today())

    def __str__(self):
        return self.Title
