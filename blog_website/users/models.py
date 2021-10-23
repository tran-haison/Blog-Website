from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    # Map Profile -> User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Set profile's image with default = 'default.jpg' and path to directory 'profile_pic'
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    # Function to display string
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        # Resize image to smaller size
        img = Image.open(self.image.path)
        if (img.height > 300 or img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
