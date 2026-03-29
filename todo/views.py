
# Create your views here.
from rest_framework import generics
from .models import ToDo
from todo.apis.serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer