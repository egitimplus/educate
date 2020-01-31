from django.db import models


class ComponentRelationship(models.Model):
    component = models.ForeignKey('components.Component', related_name='component_source', on_delete=models.CASCADE)
    parent = models.ForeignKey('components.Component', related_name='component_target', on_delete=models.CASCADE)

    class Meta:
        db_table = 'components_component_component'
