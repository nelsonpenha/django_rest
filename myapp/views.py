from django.shortcuts import render
from .models import Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista.html', {'estudiantes': estudiantes})


from rest_framework import viewsets
from .models import Estudiante, Carrera
from .serializers import CarreraSerializer, EstudianteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EstudianteFilter

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstudianteFilter


#from rest_framework import viewsets, mixins

#class EstudianteViewSet(mixins.ListModelMixin,
 #                        mixins.CreateModelMixin,
  #                       mixins.RetrieveModelMixin,
   ##                     viewsets.GenericViewSet):
    #queryset = Estudiante.objects.all()
    #serializer_class = EstudianteSerializer




#UpdateModelMixin
#DestroyModelMixin