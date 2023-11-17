from django.http import JsonResponse
from .models import Curso
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    contex = {
        "status": True,
        "content": "mi primer api rest con django"
    }

    return JsonResponse(contex)

@csrf_exempt
def cursos(request):
    listado_cursos = Curso.objects.all()

    context = {
        "status": True,
        "content": list(listado_cursos.values())
    }

    return JsonResponse(context)

@csrf_exempt
def post_curso(request):
    json_data = json.loads(request.body)
    
    titulo = json_data["titulo"]
    description = json_data["description"]
    imagen = json_data["imagen"]

    nuevo_curso = Curso.objects.create(
        titulo=titulo,
        description=description,
        imagen=imagen
    )
    """CREO UN DICCIONARIO(JSON) PARA PODER MOSTRAR 
    LOS DATOS DEL NUEVO OBJETO CREADO (nuevo_curso) 
    Y PASO ESTE DICCIONARIO AL CONTEXT"""

    salida_curso_json = {
        "id": nuevo_curso.id,
        "titulo": nuevo_curso.titulo,
        "description": nuevo_curso.description,
        "imagen": nuevo_curso.imagen
    }

    context = {
        "status": True,
        "content": "nuevo registro creado",
        "regitro": salida_curso_json
    }

    return JsonResponse(context)

"""IMPLEMENTACION DE DJANGORESTFRAMEWORK(DRF)"""
from rest_framework import generics
from rest_framework import serializers

"""esta clase permitirá mapear y conectar al modelo Curso con un serializador para convertir en datos JSON"""
class CursoSerializer(serializers.ModelSerializer):   
    class Meta:                                       # Meta se utilizapara brindar metainformacion sobre la subclase principal(CursoSerializer)
        model = Curso                                 # Esta propiedad indica que este serializador esta asociado con el modelo Curso
        fields = "__all__"                            # Esto significa que el serializador incluirá todos los campos del modelo Curso


"""Vista basade en clases"""
class CursoList(generics.ListCreateAPIView): # la clase CursoList hereda de generics.ListCreateAPIView. Esta representa una vista que manejará las solicitudes (GET) y (POST) modelo Curso.
    queryset = Curso.objects.all()           # especifica la consulta que se hara al modelo Curso para mostrar las instancias en la lista.
    serializers_class = CursoSerializer      # indica el serializador que se utilizará para serializar y deserializar las instancias del modelo Curso                                        
                                                    