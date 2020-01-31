from django.db import models

'''
Üniversite burs indirimleri
'''


class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)