# Generated by Django 3.0.3 on 2020-03-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publishers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('seconds', models.SmallIntegerField(default=0)),
                ('level', models.SmallIntegerField(choices=[(1, 'Çok Kolay'), (2, 'Kolay'), (3, 'Orta'), (4, 'Zor'), (5, 'Çok Zor')], default=1)),
                ('question_start_type', models.SmallIntegerField(choices=[(1, 'Yazı'), (2, 'Resim'), (3, 'Livescribe'), (4, 'Video'), (5, 'PDF')], default=1)),
                ('question_start_value', models.TextField()),
                ('question_answer_type', models.SmallIntegerField(choices=[(1, 'Yazı'), (2, 'Resim'), (3, 'Livescribe'), (4, 'Video'), (5, 'PDF')], default=1)),
                ('question_answer_value', models.TextField()),
                ('question_pattern', models.SmallIntegerField(default=0)),
                ('active', models.SmallIntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'questions_question',
                'permissions': (('view_question', 'View question'), ('list_question', 'List questions')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_type', models.SmallIntegerField()),
                ('answer_value', models.TextField()),
                ('answer_choice', models.SmallIntegerField()),
                ('is_true_answer', models.SmallIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'questions_question_answer',
                'permissions': (('view_questionanswer', 'View question answer'), ('list_questionanswer', 'List question answers')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswerStat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_is_true', models.SmallIntegerField()),
                ('answer_seconds', models.SmallIntegerField()),
                ('answer_type', models.SmallIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'questions_question_answer_stat',
                'permissions': (('view_questionanswerstat', 'View question answer stat'), ('list_questionanswerstat', 'List question answer stat')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.SmallIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'questions_question_exam',
                'permissions': (('view_questionexam', 'View question exam'), ('list_questionexam', 'List question exam')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionUnique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_code', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'questions_question_unique',
                'permissions': (('view_questionunique', 'View question unique'), ('list_questionunique', 'List question unique')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionUniqueStat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_code', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField()),
                ('answers', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'questions_question_unique_stat',
                'permissions': (('view_questionuniquestat', 'View question unique stat'), ('list_questionuniquestat', 'List question unique stat')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='UserQuestionAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('check', models.SmallIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_question_answer_question', to='questions.Question')),
                ('source', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_question_answer_source', to='publishers.Source')),
            ],
            options={
                'db_table': 'questions_user_question_answers',
                'permissions': (('view_userquestionanswer', 'View user question answer'), ('list_userquestionanswer', 'List user question answer')),
                'default_permissions': (),
            },
        ),
    ]
