from companies.models import Company
from django.db import models
from django.template.defaultfilters import slugify
import itertools


class Publisher(Company):
    group = models.ForeignKey('companies.CompanyGroup', related_name='publisher_group', on_delete=models.CASCADE)
    manager = models.ManyToManyField('users.User', through='PublisherManager', related_name='publisher_managers')

    class Meta:
        default_permissions = ()
        permissions = (
            ("view_publisher", "View publisher"),
            ("list_publisher", "List publisher"),
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not Publisher.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(Publisher, self).save()
