import django_filters
from apps.tareas.models import *

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Tarea
        fields = [
            'status',  
        ]