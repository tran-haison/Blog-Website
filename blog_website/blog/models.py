from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Class "Post" is defined as table "Post" in db, extends Model class
class Post(models.Model):
    # Define columns

    # Title
    title = models.CharField(max_length=100)

    # Content
    content = models.TextField()

    # Date posted (automatically created by default)
    date_posted = models.DateTimeField(default=timezone.now)

    # Author
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title