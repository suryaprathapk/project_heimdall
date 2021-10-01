from django.db import models


# Create your models here.
class Technologies(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()

    # Image = models.ImageField(upload_to ='images/')
    # manual_EOL_date = models.CharField(max_length =100)

    def __str__(self):
        return self.Title
