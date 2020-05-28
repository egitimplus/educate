from django.db import models
from library.constant import LEVEL, TYPES


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    seconds = models.SmallIntegerField(default=0)
    level = models.SmallIntegerField(choices=LEVEL, default=1)
    question_start_type = models.SmallIntegerField(choices=TYPES, default=1)
    question_start_value = models.TextField()
    question_answer_type = models.SmallIntegerField(choices=TYPES, default=1)
    question_answer_value = models.TextField()
    question_pattern = models.SmallIntegerField(default=0)
    edu_category = models.ForeignKey('educategories.EduCategory', related_name='question_edu_category', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    active = models.SmallIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    component = models.ManyToManyField('components.Component', related_name='question_components')
    exam = models.ManyToManyField('library.Exam', related_name='question_exam', through='questions.QuestionExam')
    question_unique = models.ForeignKey('questions.QuestionUnique', related_name='question_question_unique', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    book = models.ManyToManyField('publishers.Book', related_name='question_book')
    publisher = models.ForeignKey('publishers.Publisher', related_name='question_publisher', on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        db_table = 'questions_question'
        default_permissions = ()
        permissions = (
            ("view_question", "View question"),
            ("list_question", "List questions")
        )

    @property
    def true_answer(self):
        return self.answers.filter(is_true_answer=1).first()

    @property
    def code(self):
        unique = sorted(set(self.component.all().values_list('id', flat=True)))
        return '-'.join(map(str, unique))

    '''
        selected_components için ilişkisel birşeyler lazım
        
        question_text gereksiz
        question_answer gereksiz
    '''
