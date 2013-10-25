from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class Language(models.Model):
    lang = models.CharField(max_length=30)
    freebase_id = models.CharField(max_length=20)

    def __unicode__(self):
        return self.lang

class Profile(models.Model):
    user = models.OneToOneField(User, editable=False)
    languages = models.ManyToManyField(Language,
        related_name = 'lang+'
    )
    active_language = models.ForeignKey(Language,
        null = True,
        related_name ='active+',
    )

    def __unicode__(self):
        return self.user.username

class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('languages',)

class ActiveLanguageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('active_language',)

    def __init__(self, *args, **kwargs):
        added = kwargs.pop('added', [])
        super(ActiveLanguageForm, self).__init__(*args, **kwargs)
        if added:
            self.fields['active_language'].empty_label = None
            self.fields['active_language'].queryset = added

@receiver(post_save, sender=User)
def create_new_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()

@receiver(post_save, sender=Profile)
def update_languages(sender, created, instance, **kwargs):
    active_language = instance.active_language
    if not active_language:
        return

    try:
        instance.languages.get(lang=active_language.lang)
    except ObjectDoesNotExist:
        instance.languages.add(active_language)