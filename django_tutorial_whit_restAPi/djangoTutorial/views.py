from django.http import JsonResponse
from .models import Curso
import json
# Create your views here.

def index(request):
    contex = {
        "status": True,
        "content": "mi primer api rest con django"
    }

    return JsonResponse(contex)


def cursos(request):
    listado_cursos = Curso.objects.all()

    context = {
        "status": True,
        "content": list(listado_cursos.values())
    }

    return JsonResponse(context)


def post_curso(request):
    json_data = json.loads(request.body)
    
    titulo = json_data["titulo"]
    descripcion = json_data["descripcion"]
    imagen = json_data["imagen"]

    nuevo_curso = Curso.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        imagen=imagen
    )

    context = {
        "status": True,
        "content": "nuevo registro creado"
    }

    return JsonResponse(context)