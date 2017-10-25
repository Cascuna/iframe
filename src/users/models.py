from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
import os
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    description = models.CharField(
        _('Description'), max_length=150, help_text=_('Add a sassy description for your profile'), blank=True)
    avatar = models.ImageField(
        upload_to=os.path.join(settings.FILE_UPLOAD_PATH, 'display_pictures'), max_length=500, blank=True)

    def __str__(self):
        return str(self.user.username)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver, settings.AUTH_USER_MODEL)