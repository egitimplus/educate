from django.db import models


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sort_order = models.SmallIntegerField()
    active = models.SmallIntegerField()



