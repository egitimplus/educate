from django.db import models


class SchoolBook(models.Model):
    book = models.ForeignKey('publishers.Book', on_delete=models.CASCADE)
    school = models.ForeignKey('companies.School', on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies_school_book'
