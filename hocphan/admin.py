from django.contrib import admin
from .models import Majors
from .models import Subjects
from .models import Docs

# Register your models here.
admin.site.register(Majors)
admin.site.register(Subjects)
admin.site.register(Docs)

