from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class LearningLectureContent(models.Model):
    id = models.AutoField(primary_key=True)
    lecture = GenericRelation('curricula.LearningLecture')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class LearningLectureVideo(LearningLectureContent):
    media = models.ForeignKey('library.Media', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        db_table = 'curricula_learning_lecture_video'
        default_permissions = ()
        permissions = (
            ("view_learninglecturevideo", "View learning lecture video"),
            ("list_learninglecturevideo", "List learning lecture video")
        )


class LearningLectureLiveScribe(LearningLectureContent):
    media = models.ForeignKey('library.Media', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        db_table = 'curricula_learning_lecture_livescribe'
        default_permissions = ()
        permissions = (
            ("view_learninglecturelivescribe", "View learning lecture livescribe"),
            ("list_learninglecturelivescribe", "List learning lecture livescribe")
        )


class LearningLectureText(LearningLectureContent):
    content = models.TextField()

    class Meta:
        db_table = 'curricula_learning_lecture_text'
        default_permissions = ()
        permissions = (
            ("view_learninglecturetext", "View learning lecture text"),
            ("list_learninglecturetext", "List learning lecture text")
        )


class LearningLectureYoutube(LearningLectureContent):

    name = models.CharField(max_length=255)
    desc = models.TextField()
    file = models.CharField(max_length=255)

    class Meta:
        db_table = 'curricula_learning_lecture_youtube'
        default_permissions = ()
        permissions = (
            ("view_learninglectureyoutube", "View learning lecture youtube"),
            ("list_learninglectureyoutube", "List learning lecture youtube")
        )