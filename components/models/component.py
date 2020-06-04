from django.db import models


class Component(models.Model):
    id = models.AutoField(primary_key=True)
    edu_category = models.ForeignKey('educategories.EduCategory', related_name='component_category',
                                     on_delete=models.SET_NULL, default=None, blank=True, null=True)
    name = models.CharField(max_length=255)
    level = models.SmallIntegerField(default=1)
    active = models.SmallIntegerField(default=1)
    group = models.SmallIntegerField(default=0)
    seconds = models.SmallIntegerField(default=150)
    file = models.TextField(default=None, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    to_component = models.ManyToManyField('self', related_name='source_component', through='components.ComponentRelationship',
                                          symmetrical=False, through_fields=('component', 'parent'))

    class Meta:
        db_table = 'components_component'
        default_permissions = ()
        permissions = (
            ("super_component", ""), # ComponentViewSet@all
            ("view_component", ""), # ComponentViewSet@retrieve
            ("add_component", ""), # ComponentViewSet@create
            ("change_component", ""), # ComponentViewSet@update
            ("delete_component", ""), # ComponentViewSet@destroy
            ("list_components", ""), # ComponentViewSet@list
            ("user_detail_component", ""), # ComponentViewSet@user_detail
            ("search_component", ""), # ComponentViewSet@search
            ("parents_component", "") # ComponentViewSet@parents
        )

    def __str__(self):
        return self.name
