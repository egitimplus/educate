# Generated by Django 3.0.3 on 2020-05-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_questionuniquestat_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionuniquestat',
            name='answers',
            field=models.TextField(default='[]'),
        ),
    ]
