# Generated by Django 3.0.3 on 2020-03-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.SmallIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'permissions': (('view_book', 'View book'), ('list_book', 'List book')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.PositiveSmallIntegerField(default=1)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'permissions': (('view_publisher', 'View publisher'), ('list_publisher', 'List publisher')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PublisherManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'publishers_publisher_manager',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('sort_order', models.SmallIntegerField(default=0)),
                ('active', models.SmallIntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_book', to='publishers.Book')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_parent', to='publishers.Source')),
            ],
            options={
                'permissions': (('view_source', 'View source'), ('list_source', 'List source')),
                'default_permissions': (),
            },
        ),
    ]
