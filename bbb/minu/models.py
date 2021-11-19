from django.db import models
from django.conf import settings

# Create your models here.


class Review(models.Model):
    name = models.ForeignKey(
         settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE, default=''
    )
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    audio= models.FileField(upload_to='audios/%Y/%m/%d/', blank=True)
    date = models.CharField(max_length=50,default='')
    users_in = models.CharField(max_length=50,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-id"]
