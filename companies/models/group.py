from django.db import models
from django.template.defaultfilters import slugify
import itertools
from django.contrib.contenttypes.fields import GenericRelation


class CompanyGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    user = models.ForeignKey('users.User', related_name='group_manager', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    pattern = GenericRelation('users.Pattern')

    class Meta:
        default_permissions = ()
        permissions = (
            ("super_companygroup", "All access for company group"),  # CompanyViewSet@all
            ("add_companygroup", "Add company group"), # CompanyViewSet@create
            ("change_companygroup", "Change company group"), # CompanyViewSet@update
            ("delete_companygroup", "Delete access for company group"), # CompanyViewSet@destroy
            ("view_companygroup", "View company group"),  # CompanyViewSet@retrieve
            ("list_companygroups", "List company group"),  # CompanyViewSet@list
            ("list_companygroup_schools", 'List company group schools'),  # CompanyViewSet@school_list
            ("list_companygroup_publishers", 'List company group publishers')  # CompanyViewSet@publisher_list
        )


    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not CompanyGroup.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(CompanyGroup, self).save()
