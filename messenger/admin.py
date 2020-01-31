from django.contrib import admin
from messenger.models import *

# Register your models here.
admin.site.register(Message)
admin.site.register(Participiant)
admin.site.register(Reply)
admin.site.register(ReplyAnswer)
admin.site.register(Thread)

