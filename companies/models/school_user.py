from django.db import models


class SchoolUser(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_user'
