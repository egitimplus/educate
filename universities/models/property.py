from django.db import models

'''
Özellikler
'''


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey('universities.Department', related_name='property_department', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

