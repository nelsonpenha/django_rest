import django_filters
from .models import Estudiante

class EstudianteFilter(django_filters.FilterSet):
    # Filtros de carrera
    carrera__id = django_filters.NumberFilter(field_name='carrera__id', label='ID de la carrera')
    carrera__nombre = django_filters.CharFilter(field_name='carrera__nombre', lookup_expr='icontains', label='Nombre de la carrera')
    carrera__duracion = django_filters.NumberFilter(field_name='carrera__duracion', label='Duración de la carrera (años)')

    # Filtros de estudiante
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains', label='Nombre del estudiante')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains', label='Email del estudiante')
    edad = django_filters.NumberFilter(field_name='edad', label='Edad del estudiante')
    edad__gte = django_filters.NumberFilter(field_name='edad', lookup_expr='gte', label='Edad mínima')
    edad__lte = django_filters.NumberFilter(field_name='edad', lookup_expr='lte', label='Edad máxima')

    class Meta:
        model = Estudiante
        fields = [
            'nombre', 'email', 'edad', 'edad__gte', 'edad__lte',
            'carrera__id', 'carrera__nombre', 'carrera__duracion'
        ]