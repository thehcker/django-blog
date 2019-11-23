from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

# def post_save_profile_receiver(sender, instance, *args, **kwargs):
# 		profile_obj, new_obj = Profile.objects.get_or_create(user=instance)
# post_save.connect(pre_save_profile_receiver, sender=User)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
# 	instance.profile.save()