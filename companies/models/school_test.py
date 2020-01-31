from django.db import models


class SchoolTest(models.Model):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_test'


