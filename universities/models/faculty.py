from django.db import models

'''
Fakülteler
'''


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.ForeignKey('library.Province', related_name='faculty_province', on_delete=models.CASCADE)
    university = models.ForeignKey('universities.University', related_name='faculty_university', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    is_undergraduate = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
