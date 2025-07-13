from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    watched_quotes = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(protocol='both',unpack_ipv4=False,null=True,blank=True)
    liked_quotes = models.JSONField(default=dict)
    disliked_quotes = models.JSONField(default=dict)

