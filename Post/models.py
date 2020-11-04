from django.db import models
from django.urls import reverse
from django.contrib.auth.forms import User


class Post(models.Model):
    image = models.ImageField(upload_to='post/%Y/%m', height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE, default=2)
    like = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = ('like', 'post')


class Comment(models.Model):
    c_post = models.ForeignKey(Post, related_name='c_post', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, default=2)
    comment = models.CharField(max_length=500)
