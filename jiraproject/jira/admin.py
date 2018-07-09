from django.contrib import admin

from .models import Company
from .models import Project
from.models import user1
from.models import Modules


admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Modules)
admin.site.register(user1)

# Register your models here.
