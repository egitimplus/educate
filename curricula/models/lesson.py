from django.db import models
from django.template.defaultfilters import slugify
import itertools

"""
Domain      : Geometri
SubDomain   : Üçgenler
Subject     : Üçgenlerde Temel Kavramlar
"""


class LearningLesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    active = models.PositiveSmallIntegerField()
    public = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    edu_category = models.ForeignKey('educategories.EduCategory', related_name='lesson_edu_category', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        db_table = 'curricula_learning_lesson'
        default_permissions = ()
        permissions = (
            ("view_learninglesson", "View learning lesson"),
            ("list_learninglesson", "List learning lesson")
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not LearningLesson.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(LearningLesson, self).save()
