from django.db import models

# Create your models here.
class Viewer(models.Model):
    """Модель зрителя"""
    watched_quotes = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(protocol='both',unpack_ipv4=False,null=True,blank=True)
    liked_quotes = models.JSONField(default=dict)
    disliked_quotes = models.JSONField(default=dict)