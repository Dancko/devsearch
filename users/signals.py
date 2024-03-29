from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .models import Profile


@receiver(post_save, sender=User)
def createUser(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, 
            username=user.username,
            email=user.email,
            name=user.first_name
        )

        subject = 'Welcome to DevSearch'
        message = "we are glad that you are here."

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )



@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

@receiver(post_save, sender=Profile)
def editUser(sender, instance, created, **kwargs):
    profile = instance 
    user = profile.user
    if created == False:
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.name 
        user.save()
    
