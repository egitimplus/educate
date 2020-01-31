from django.db import models

'''
Üniversite sınav türleri
Bu başka applerde de kullanılıyor
Başka bir yere mi taşımalı ? Nasıl yapılıyor.
'''


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
