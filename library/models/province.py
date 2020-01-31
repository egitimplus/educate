from django.db import models


class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
