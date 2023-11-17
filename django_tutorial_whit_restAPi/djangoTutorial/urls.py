from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("cursos", views.cursos),
    path("cursos/new", views.post_curso)
]
