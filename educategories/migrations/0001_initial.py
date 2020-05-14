# Generated by Django 3.0.3 on 2020-03-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EduCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('depth', models.SmallIntegerField(default=0)),
                ('active', models.SmallIntegerField(default=1)),
                ('sort_category', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('lesson', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edu_category_lesson', to='educategories.EduCategory')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edu_category_parent', to='educategories.EduCategory')),
                ('subject', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edu_category_subject', to='educategories.EduCategory')),
                ('unit', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edu_category_unit', to='educategories.EduCategory')),
            ],
            options={
                'db_table': 'educategories_edu_categories',
                'permissions': (('view_educategory', 'View educate category'), ('list_educategory', 'List educate category')),
                'default_permissions': (),
            },
        ),
    ]