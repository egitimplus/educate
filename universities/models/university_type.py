from django.db import models

'''
Üniversite tipleri
'''


class UniversityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'universities_university_type'