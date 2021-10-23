from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Create receiver here


# When User sends a signal which is 'post_save'
# Receiver will be triggered -> this function will be executed
# 4 parameters will be passed by receiver
# Then check if User was created -> if YES, create a new corresponding Profile with new User instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Same as above function but this will save Profile to db
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()