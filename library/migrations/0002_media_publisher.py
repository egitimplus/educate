# Generated by Django 3.0.3 on 2020-03-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publishers', '0001_initial'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='publisher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='publishers.Publisher'),
        ),
    ]
