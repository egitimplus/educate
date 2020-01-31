from django.db import models


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField()
    user = models.ForeignKey('users.User', related_name='message_user', on_delete=models.CASCADE)
    thread = models.ForeignKey('messenger.Thread', related_name='message_thread', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

