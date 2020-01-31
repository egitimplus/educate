from django.db import models

'''
Çözülen test raporları
'''


class Report(models.Model):
    id = models.AutoField(primary_key=True) 
    report = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    types = models.ManyToManyField('tests.Test', through='tests.ReportType')

    class Meta:
        default_permissions = ()
        permissions = (
            ("view_report", "View test report"),
            ("list_report", "List test report")
        )
