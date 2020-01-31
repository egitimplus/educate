from django.db import models


class ReportType(models.Model):
    # bunun ne olduguna bakalım. eski veritabanında vardı. ama kullanılıyor mu?
    test = models.ForeignKey('tests.Test', related_name='report_type_test', on_delete=models.CASCADE)
    report = models.ForeignKey('tests.Report', related_name='report_type_report', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'tests_report_type'
        default_permissions = ()
        permissions = (
            ("view_reporttype", "View test report type"),
            ("list_reporttype", "List test report type")
        )