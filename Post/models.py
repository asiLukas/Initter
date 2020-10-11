from django.db import models
from django.urls import reverse
from django.contrib.auth.forms import User


class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='post/%Y/%m', height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
