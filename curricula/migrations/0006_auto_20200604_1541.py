# Generated by Django 3.0.3 on 2020-06-04 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curricula', '0005_auto_20200531_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learninglecture',
            name='component',
        ),
        migrations.RemoveField(
            model_name='learningunit',
            name='component',
        ),
    ]
