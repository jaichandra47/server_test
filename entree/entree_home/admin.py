from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .models import Query
admin.site.register(Query)

