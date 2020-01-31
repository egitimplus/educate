from django.db import models


class ComponentStat(models.Model):
    id = models.AutoField(primary_key=True)
    component = models.ForeignKey('components.Component', related_name='component_stat_component', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='component_stat_user', on_delete=models.CASCADE)
    component_status = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'components_component_stat'
        default_permissions = ()
        permissions = (
            ("view_componentstat", "View component stat"),
            ("list_componentstat", "List component stat")
        )
