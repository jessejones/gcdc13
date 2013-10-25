from django.db import models
from django.forms import ModelForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Language(models.Model):
    lang = models.CharField(max_length=30)
    freebase_id = models.CharField(max_length=20)

    def __unicode__(self):
        return self.lang

class Profile(models.Model):
    user = models.OneToOneField(User, editable=False)
    languages = models.ManyToManyField(Language)

    def __unicode__(self):
        return self.user.username

class ProfileForm(ModelForm):
    class Meta:
        model = Profile

@receiver(post_save, sender=User)
def create_new_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()