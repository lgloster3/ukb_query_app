from django.contrib import admin
from . models import Field

# Register your models here.
# admin.site.register(Field)
# admin.site.register(Event)

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Field._meta.get_fields()]
    ordering = ('field_id',)
    search_fields = ('field_id','title')