from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
import itertools


class LearningUnit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    position = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    test = GenericRelation('curricula.LearningTest')
    domain = models.ForeignKey('curricula.LearningDomain', on_delete=models.CASCADE)
    lesson = models.ForeignKey('curricula.LearningLesson', related_name='units', related_query_name='unit', on_delete=models.CASCADE)
    component = models.ManyToManyField('components.Component', related_name='unit_component')

    class Meta:
        db_table = 'curricula_learning_unit'
        default_permissions = ()
        permissions = (
            ("view_learningunit", "View learning unit"),
            ("list_learningunit", "List learning unit"),
            ("view_learningunit_test", "View learning unit test"),
            ("list_learningunit_test", "List learning unit test"),
            ("add_learningunit_test", "Attach learning unit test"),
            ("delete_learningunit_test", "Detach learning unit test")
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not LearningUnit.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(LearningUnit, self).save()