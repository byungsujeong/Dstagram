from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField(default='')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + ', ' + self.created.strftime('%Y-%m-%d %H:%M:$S')


