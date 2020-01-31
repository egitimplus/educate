from django.db import models


class Participiant(models.Model):
    id = models.AutoField(primary_key=True)
    trashed = models.SmallIntegerField()
    last_read = models.DateField()
    user = models.ForeignKey('users.User', related_name='participiant_user', on_delete=models.CASCADE)
    thread = models.ForeignKey('messenger.Thread', related_name='participiant_thread', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

