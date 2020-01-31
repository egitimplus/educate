from django.db import models


class SchoolType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'companies_school_type'