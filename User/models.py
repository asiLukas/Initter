from django.db import models
from django.contrib.auth.forms import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_picture/%Y/%m', width_field='width_field',
                                    height_field='height_field')
    description = models.TextField(default='', max_length=150)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Following(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE, default=2)
    follow = models.ForeignKey(User, related_name='follow', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return 'Follower: %s, Follows: %s' % (self.follower, self.follow)

    class Meta:
        unique_together = ('follower', 'follow')

