from django.db import models
from django.template.defaultfilters import slugify
import itertools


class Source(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', related_name='source_parent', on_delete=models.CASCADE, default=None, blank=True, null=True)
    book = models.ForeignKey('publishers.Book', related_name='source_book', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_order = models.SmallIntegerField(default=0)
    active = models.SmallIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    question = models.ManyToManyField('questions.Question', related_name='source_questions')

    class Meta:
        default_permissions = ()
        permissions = (
            ("view_source", "View source"),
            ("list_source", "List source"),
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not Source.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(Source, self).save()