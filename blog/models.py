from django.db import models


class TGUser(models.Model):
    tg_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    is_married = models.BooleanField(default=False)
    birth_day = models.DateField()
    email = models.EmailField()
    website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

