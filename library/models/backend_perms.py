from django.db import models


class BackendPerms(models.Model):
    id = models.AutoField(primary_key=True)
    view_name = models.CharField(max_length=50)
    view_action = models.CharField(max_length=50)
    permission_name = models.CharField(max_length=100)



