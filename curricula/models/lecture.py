from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.defaultfilters import slugify
import itertools
from django.contrib.contenttypes.fields import GenericRelation


class LearningLecture(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    summary = models.CharField(max_length=255)
    practice = models.ForeignKey('tests.Test', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    content = models.TextField()
    position = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    subject = models.ForeignKey('curricula.LearningSubject', related_name='lecture_parent', on_delete=models.CASCADE)
    tag = models.ManyToManyField('curricula.LearningTag', related_name='lecture_tag')

    publisher = models.ForeignKey('publishers.Publisher', related_name='lecture_publisher', on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'curricula_learning_lecture'
        default_permissions = ()
        permissions = (
            ("view_learninglecture", "View learning lecture"),
            ("list_learninglecture", "List learning lecture"),
            ("view_learninglecture_test", "View learning lecture test"),
            ("add_learninglecture_test", "Attach learning lecture test"),
            ("delete_learninglecture_test", "Detach learning lecture test")
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not LearningLecture.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(LearningLecture, self).save()



