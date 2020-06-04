from django.db import models


class SchoolUser(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_user'
        default_permissions = ()
        permissions = (
            ("add_school_user", 'Attach user to school'), # SchoolViewSet@attach_user
            ("delete_school_user", 'Detach user from school'),  # SchoolViewSet@detach_user
            ("list_school_users", "List school users"),  # SchoolViewSet@user_list
        )

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
