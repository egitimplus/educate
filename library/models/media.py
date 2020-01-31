from django.db import models


class Media(models.Model):
    id = models.AutoField(primary_key=True)
    media_name = models.CharField(max_length=255)
    media_desc = models.TextField(default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    media_file = models.FileField(upload_to='files/%Y/%m/%d/', default=None)
    publisher = models.ForeignKey('publishers.Publisher', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __str__(self):
        return "%s" % self.media_name




