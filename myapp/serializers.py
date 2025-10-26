from rest_framework import serializers
from .models import Estudiante, Carrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    # Mostrar el detalle de la carrera a la que pertenece el estudiante
    carrera = CarreraSerializer(read_only=True)
    # Permitir asignar carrera por ID
    carrera_id = serializers.PrimaryKeyRelatedField(
        queryset=Carrera.objects.all(),
        source='carrera',
        write_only=True
    )

    class Meta:
        model = Estudiante
        fields = '__all__'
        #fields = ['id', 'nombre', 'edad', 'email', 'carrera', 'carrera_id']
