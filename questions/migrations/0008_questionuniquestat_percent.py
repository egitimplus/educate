# Generated by Django 3.0.3 on 2020-05-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20200503_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionuniquestat',
            name='percent',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
