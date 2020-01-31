from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
import itertools


class LearningDomain(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    position = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    test = GenericRelation('curricula.LearningTest')

    class Meta:
        db_table = 'curricula_learning_domain'
        default_permissions = ()
        permissions = (
            ("view_learningdomain", "View learning domain"),
            ("list_learningdomain", "List learning domain"),
            ("view_learningdomain_test", "View learning domain test"),
            ("list_learningdomain_test", "List learning domain test"),
            ("add_learningdomain_test", "Attach learning domain test"),
            ("delete_learningdomain_test", "Detach learning domain test")
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not LearningDomain.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(LearningDomain, self).save()