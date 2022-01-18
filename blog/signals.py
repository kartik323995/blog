from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile

@receiver(post_save,sender=User)
def pro_create(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)
        instance.profile.save()

