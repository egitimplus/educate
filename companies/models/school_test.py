from django.db import models


class SchoolTest(models.Model):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_test'
        default_permissions = ()
        permissions = (
            ("list_school_tests", "List school tests"),  # SchoolViewSet@test_list
        )

    def __str__(self):
        return self.teacher.test
