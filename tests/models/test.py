from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

'''
Test verileri
'''


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    test_seconds = models.SmallIntegerField()
    test_start = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.SmallIntegerField(default=1)
    test_type_id = models.SmallIntegerField(default=1)

    #questions = models.ManyToManyField('questions.Question', related_name='questions')
    questions = models.ManyToManyField('questions.Question', through='TestQuestion', related_name='questions')
    categories = models.ManyToManyField('educategories.EduCategory', related_name='categories')
    publisher = models.ForeignKey('publishers.Publisher', related_name='test_publisher', on_delete=models.CASCADE)
    classroom = models.ManyToManyField('companies.Classroom', related_name='classroom')

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        default_permissions = ()
        permissions = (
            ("view_test", "View test"),
            ("list_test", "List test"),
            ("view_test_questions", "View test question"),
            ("list_test_questions", "List test questions"),
        )
