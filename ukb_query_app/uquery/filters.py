import django_filters
from django_filters import CharFilter
from .models import *

class FieldFilter(django_filters.FilterSet):
    titleFilter = CharFilter(field_name="title",lookup_expr="icontains")
    class Meta:
        model = Field
        fields = ['field_id',"instance_id","encoding_id"]