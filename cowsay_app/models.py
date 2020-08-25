from django.db import models

# Create your models here.
class User_Input(models.Model):
    text = models.CharField(max_length=120)

    def __str__(self):
        return self.text

