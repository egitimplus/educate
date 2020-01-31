from django.db import models


class ComponentStatusChange(models.Model):
    id = models.AutoField(primary_key=True)
    component = models.ForeignKey('components.Component', related_name='component_status_change_component', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='component_status_change_user', on_delete=models.CASCADE)
    old_status = models.SmallIntegerField()
    new_status = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'components_component_status_change'
        default_permissions = ()
        permissions = (
            ("view_componentstatuschange", "View component status change"),
            ("list_componentstatuschange", "List component status change")
        )