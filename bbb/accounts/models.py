from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)

    phone_number = models.CharField(
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )

    checkpw = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)




# Create your models here.
