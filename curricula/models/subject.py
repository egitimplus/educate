from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
import itertools


class LearningSubject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    position = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    test = GenericRelation('curricula.LearningTest')
    unit = models.ForeignKey('curricula.LearningUnit', related_name='subjects', related_query_name='subject', on_delete=models.CASCADE)

    class Meta:
        db_table = 'curricula_learning_subject'
        default_permissions = ()
        permissions = (
            ("view_learningsubject", "View learning subject"),
            ("list_learningsubject", "List learning subject"),
            ("view_learningsubject_test", "View learning subject test"),
            ("list_learningsubject_test", "List learning subject test"),
            ("add_learningsubject_test", "Attach learning subject test"),
            ("delete_learningsubject_test", "Detach learning subject test")
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not LearningSubject.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(LearningSubject, self).save()