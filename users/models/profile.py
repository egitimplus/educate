from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

