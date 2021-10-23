from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # Map Profile -> User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Set profile's image with default = 'default.jpg' and path to directory 'profile_pic'
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    # Function to display string
    def __str__(self):
        return f'{self.user.username} Profile'