from django.db import models
from django.template.defaultfilters import slugify
import itertools


class EduCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    depth = models.SmallIntegerField(default=0)
    active = models.SmallIntegerField(default=1)
    sort_category = models.IntegerField(default=0)
    slug = models.SlugField()
    parent = models.ForeignKey('self', related_name='edu_category_parent', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    lesson = models.ForeignKey('self', related_name='edu_category_lesson', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    subject = models.ForeignKey('self', related_name='edu_category_subject', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    unit = models.ForeignKey('self', related_name='edu_category_unit', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'educategories_edu_categories'
        default_permissions = ()
        permissions = (
            ("view_educategory", "View educate category"),
            ("list_educategory", "List educate category")
        )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None):

        if not self.id:

            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not EduCategory.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(EduCategory, self).save()