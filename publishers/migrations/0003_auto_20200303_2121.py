# Generated by Django 3.0.3 on 2020-03-03 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publishers', '0002_source_question'),
        ('library', '0002_media_publisher'),
        ('educategories', '0001_initial'),
        ('companies', '0002_auto_20200303_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publishermanager',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publishermanager',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishers.Publisher'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher_group', to='companies.CompanyGroup'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='manager',
            field=models.ManyToManyField(related_name='publisher_managers', through='publishers.PublisherManager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='exam',
            field=models.ManyToManyField(related_name='book_exams', to='library.Exam'),
        ),
        migrations.AddField(
            model_name='book',
            name='lesson',
            field=models.ManyToManyField(related_name='book_lessons', to='educategories.EduCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='publishers.Publisher'),
        ),
    ]
