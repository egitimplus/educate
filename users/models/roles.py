from django.db import models
from django.contrib.auth.models import Group


class Role(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    page = models.CharField(max_length=255)

    class Meta:
        db_table = 'users_user_group'