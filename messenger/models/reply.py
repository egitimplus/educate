from django.db import models


class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.SmallIntegerField()
    trashed = models.TextField() #Json Field
    description = models.TextField()
    file = models.CharField(max_length=255)
    user = models.ForeignKey('users.User', related_name='reply_user', on_delete=models.CASCADE)
    solver = models.ForeignKey('users.User', related_name='reply_solver_user', on_delete=models.CASCADE)
    thread = models.ForeignKey('messenger.Thread', related_name='reply_thread', on_delete=models.CASCADE)
    lesson = models.ForeignKey('companies.Lesson', related_name='reply_lesson', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

