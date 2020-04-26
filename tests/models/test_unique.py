from django.db import models


class TestUnique(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', related_name='user', on_delete=models.CASCADE)
    test = models.ForeignKey('tests.Test', related_name='tests', on_delete=models.CASCADE)
    report = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    test_result = models.SmallIntegerField()

    class Meta:
        db_table = 'tests_test_unique'
        default_permissions = ()
        permissions = (
            ("view_testunique", "View test unique"),
            ("list_testunique", "List test unique")
        )
