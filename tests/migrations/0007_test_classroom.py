# Generated by Django 3.0.3 on 2020-06-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20200531_2007'),
        ('tests', '0006_auto_20200604_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='classroom',
            field=models.ManyToManyField(related_name='classroom', to='companies.Classroom'),
        ),
    ]