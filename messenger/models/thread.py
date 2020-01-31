from django.db import models


class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    user = models.ForeignKey('users.User', related_name='thread_user', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

