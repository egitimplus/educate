from django.db import models


class ReplyAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    type = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    user = models.ForeignKey('users.User', related_name='reply_answer_user', on_delete=models.CASCADE)
    reply = models.ForeignKey('messenger.Reply', related_name='reply_answer_reply', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    class Meta:
        db_table = 'messenger_reply_answer'
