from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstarctUser
from imagekit.models import ProcessedImageField

# Create your models here.


class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
    # when someone make a new post, use this function(goes to urls.py to look for helloworld)

    def get_absolute_url(self):
        return reverse("posts_detail", args=[str(self.id)])


class InstaUser(AbstarctUser):
    proifile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
