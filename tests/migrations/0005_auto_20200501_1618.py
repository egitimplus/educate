# Generated by Django 3.0.3 on 2020-05-01 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20200425_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testunique',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', related_query_name='tes', to='tests.Test'),
        ),
    ]
