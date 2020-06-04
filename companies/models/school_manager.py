from django.db import models


class SchoolManager(models.Model):
    manager = models.ForeignKey('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_manager'
        default_permissions = ()
        permissions = (
            ("add_school_manager", 'Attach manager to school'),  # SchoolViewSet@attach_manager
            ("delete_school_manager", 'Detach manager from school'),  # SchoolViewSet@detach_manager
            ("list_school_managers","List school managers"),  # SchoolViewSet@manager_list
        )

    def __str__(self):
        return self.manager.first_name + " " + self.manager.last_name
