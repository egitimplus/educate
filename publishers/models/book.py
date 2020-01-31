from django.db import models
from django.template.defaultfilters import slugify
import itertools


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    publisher = models.ForeignKey('publishers.Publisher', related_name='book_publisher', on_delete=models.CASCADE)
    exam = models.ManyToManyField('library.Exam', related_name='book_exams')
    lesson = models.ManyToManyField('educategories.EduCategory', related_name='book_lessons')
    active = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        default_permissions = ()
        permissions = (
            ("view_book", "View book"),
            ("list_book", "List book"),
        )

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.id:
            self.slug = slugify(self.name)

            for x in itertools.count(1):
                if not Book.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, x)

        super(Book, self).save()