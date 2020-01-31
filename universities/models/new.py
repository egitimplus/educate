from django.db import models

'''
Üniversite Haberleri
'''


class New(models.Model):
    id = models.AutoField(primary_key=True)
    university = models.ForeignKey('universities.University', related_name='news_university', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, default='')
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'universities_news'
