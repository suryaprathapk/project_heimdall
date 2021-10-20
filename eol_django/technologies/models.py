from django.db import models


# Create your models here.
class Technologies(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(default='NA')
    Link = models.TextField(default='NA')
    Image = models.ImageField(upload_to='images/', default='images/default_software.png')
    manual_EOL_date = models.CharField(max_length=100, default='NA')

    def __str__(self):
        return self.Title
