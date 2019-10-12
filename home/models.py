from django.db import models

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 128)
    username = models.CharField(max_length = 20)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 20)
    profile_pic = models.ImageField(upload_to = 'images/')
    password = models.CharField(max_length = 20, default = '12345')

    def __str__(self):
        return self.username