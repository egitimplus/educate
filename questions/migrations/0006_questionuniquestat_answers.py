# Generated by Django 3.0.3 on 2020-05-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_remove_questionuniquestat_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionuniquestat',
            name='answers',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
