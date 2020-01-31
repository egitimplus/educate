from django.db import models
'''
Üniversite tablosu
'''


class University(models.Model):
    id = models.AutoField(primary_key=True)
    university_type = models.ForeignKey('universities.UniversityType', related_name='university_university_type', on_delete=models.CASCADE)
    province = models.ForeignKey('library.Province', related_name='university_province', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, default='')
    content = models.TextField()
    contact_content = models.TextField()
    slug = models.SlugField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

