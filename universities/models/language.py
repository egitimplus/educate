from django.db import models

'''
Diller
'''


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=3)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)