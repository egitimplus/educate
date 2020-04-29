# Generated by Django 3.0.3 on 2020-04-23 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200303_2121'),
        ('tests', '0002_auto_20200303_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.SmallIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test')),
            ],
            options={
                'db_table': 'tests_test_question',
            },
        ),
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(related_name='questions', through='tests.TestQuestion', to='questions.Question'),
        ),
    ]
