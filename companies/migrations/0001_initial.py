# Generated by Django 3.0.3 on 2020-03-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('year', models.PositiveSmallIntegerField()),
                ('grade', models.PositiveSmallIntegerField()),
                ('department_id', models.PositiveSmallIntegerField()),
                ('active', models.PositiveSmallIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'permissions': (('super_classroom', 'All access for classroom'), ('view_classroom', 'View Classroom'), ('add_classroom', 'Add Classroom'), ('change_classroom', 'Update Classroom'), ('delete_classroom', 'Delete Classroom'), ('list_classrooms', 'List Classroom'), ('list_classroom_students', 'List Classroom Students'), ('add_classroom_student', 'Attach Student to Classroom'), ('remove_classroom_student', 'Detach Student From Classroom'), ('list_classroom_teachers', 'List Classroom Teachers'), ('add_classroom_teacher', 'Attach Teacher to Classroom'), ('remove_classroom_teacher', 'Detach Teacher From Classroom'), ('add_classroom_lesson', 'Attach Lesson to Classroom '), ('delete_classroom_lesson', 'Detach Lesson From Classroom'), ('view_classroom_teacher', 'View Classroom Teacher'), ('view_classroom_student', 'View Classroom Student'), ('change_classroom_lesson', 'Change Classroom Lesson'), ('view_classroom_lesson', 'View Classroom Lesson'), ('list_classroom_lessons', 'List Classroom Lesson')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ClassroomLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_classroom_lesson',
            },
        ),
        migrations.CreateModel(
            name='ClassroomStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_classroom_student',
            },
        ),
        migrations.CreateModel(
            name='ClassroomTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_classroom_teacher',
            },
        ),
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active', models.PositiveSmallIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'permissions': (('super_companygroup', 'All access for company group'), ('add_companygroup', 'Add company group'), ('change_companygroup', 'Change company group'), ('delete_companygroup', 'Delete access for company group'), ('view_companygroup', 'View company group'), ('list_companygroups', 'List company group'), ('list_companygroup_schools', 'List company group schools'), ('list_companygroup_publishers', 'List company group publishers')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'permissions': (('super_lesson', 'List lesson'), ('add_lesson', 'List lesson'), ('change_lesson', 'List lesson'), ('delete_lesson', 'List lesson'), ('list_lessons', 'List lesson'), ('view_lesson', 'List lesson'), ('attach_lesson_teacher', 'Add lesson teacher'), ('detach_lesson_teacher', 'Detach lesson teacher'), ('update_lesson_classroom', 'Update lesson teacher'), ('list_lesson_teacher', 'List lesson teachers')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active', models.PositiveSmallIntegerField(default=1)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('code', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'permissions': (('super_school', 'Super school'), ('add_school', 'Add school'), ('change_school', 'Update school'), ('update_school', 'Update school'), ('delete_school', 'Delete school'), ('view_school', 'View school'), ('list_schools', 'List school'), ('list_school_classrooms', 'View school classroom list'), ('list_school_lessons', 'List school lessons'), ('list_school_lesson_teachers', 'List school lesson teachers'), ('filter_school_lesson_teachers', 'List school lesson teachers'), ('add_school_manager', 'Attach manager to school'), ('delete_school_manager', 'Detach manager from school'), ('list_school_managers', 'List school managers'), ('add_school_student', 'Attach student to school'), ('delete_school_student', 'Detach student from school'), ('list_school_students', 'List school students'), ('add_school_teacher', 'Attach teacher to school'), ('delete_school_teacher', 'Detach teacher from school'), ('list_school_teachers', 'List school teachers'), ('add_school_user', 'Attach user to school'), ('delete_school_user', 'Detach user from school'), ('list_school_users', 'List school users'), ('list_school_tests', 'List school tests'), ('update_school_roles', 'Update school roles')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SchoolBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_school_book',
            },
        ),
        migrations.CreateModel(
            name='SchoolLessonTeacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('duration', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'companies_school_lesson_teacher',
            },
        ),
        migrations.CreateModel(
            name='SchoolManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_school_manager',
            },
        ),
        migrations.CreateModel(
            name='SchoolStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_school_student',
            },
        ),
        migrations.CreateModel(
            name='SchoolTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_school_teacher',
            },
        ),
        migrations.CreateModel(
            name='SchoolTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'companies_school_test',
            },
        ),
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'companies_school_type',
            },
        ),
        migrations.CreateModel(
            name='SchoolUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.School')),
            ],
            options={
                'db_table': 'companies_school_user',
            },
        ),
    ]
