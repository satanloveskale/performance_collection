from django.contrib import admin
from .models import Score, Name, Subject
from django.views.generic.list import ListView
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ScoreResource(resources.ModelResource):

    class Meta:
        model = Score
        skip_unchanged = True
        report_skipped = False

class NameResource(resources.ModelResource):

    class Meta:
        model = Name

class SubjectResource(resources.ModelResource):

    class Meta:
        model = Subject

class ScoreAdmin(ImportExportModelAdmin):
    resource_class = ScoreResource

class NameAdmin(ImportExportModelAdmin):
    resource_class = NameResource
    list_display = ( 'author', 'id')

class SubjectAdmin(ImportExportModelAdmin):
    resource_class = SubjectResource
    list_display = ( 'author', 'id')

admin.site.register(Score, ScoreAdmin)
admin.site.register(Name, NameAdmin)
admin.site.register(Subject, SubjectAdmin)