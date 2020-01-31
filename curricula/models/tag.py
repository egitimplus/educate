from django.db import models
from django.template.defaultfilters import slugify
import itertools


class LearningTag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        db_table = 'curricula_learning_tag'
        default_permissions = ()
        permissions = (
            ("view_learningtag", "View learnimg tag"),
            ("list_learningtag", "List learning tag")
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not LearningTag.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(LearningTag, self).save()