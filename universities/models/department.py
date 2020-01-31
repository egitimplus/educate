from django.db import models

'''
Departmanlar
'''


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.ForeignKey('universities.Section', related_name='universities_section', on_delete=models.CASCADE)
    language = models.ForeignKey('universities.Language', related_name='universities_language', on_delete=models.CASCADE)
    discount = models.ForeignKey('universities.Discount', related_name='universities_discount', on_delete=models.CASCADE)
    tag = models.ForeignKey('universities.Tag', related_name='universities_tag', on_delete=models.CASCADE)
    faculty = models.ForeignKey('universities.Faculty', related_name='universities_faculty', on_delete=models.CASCADE)
    title = models.CharField(max_length=255) # bu ayrıca tag tablosunda da var.
    slug = models.SlugField()
    content = models.TextField()
    education_type = models.SmallIntegerField()
    base_point = models.CharField(max_length=10)
    ranking = models.CharField(max_length=10)
    is_undergraduate = models.SmallIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    condition = models.ManyToManyField('universities.Condition', related_name='department_conditions')

