from django.contrib import admin
from .models import Project

# Register your models here.
#se muestra fecah de creacion de cada archivo
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)