from django.contrib import admin
from publishers.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Source)