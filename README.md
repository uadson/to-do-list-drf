# to-do-list-drf
## Primeiros passos na construção de um projeto com Django Rest Framework
#### Getting Started in Building a Project with Django Rest Framework


Projeto fundamentado no conteúdo disponível na plataforma Udemy - [Aprenda Django REST Framework do Zero](https://www.udemy.com/course/aprenda-django-rest-framework-do-zero/)
*Project based on the content available on the Udemy platform - [Aprenda Django REST Framework do Zero](https://www.udemy.com/course/aprenda-django-rest-framework-do-zero/)*

[Documentação Oficial](https://www.django-rest-framework.org/)

*[Official Documentation](https://www.django-rest-framework.org/)*


[![Build Status](https://app.travis-ci.com/uadson/to-do-list-drf.svg?branch=main)](https://app.travis-ci.com/uadson/to-do-list-drf)    [![Updates](https://pyup.io/repos/github/uadson/to-do-list-drf/shield.svg)](https://pyup.io/repos/github/uadson/to-do-list-drf/)    [![Python 3](https://pyup.io/repos/github/uadson/to-do-list-drf/python-3-shield.svg)](https://pyup.io/repos/github/uadson/to-do-list-drf/)


1. Instalação / Instalation

	pip install djangorestframework


### Modelo básico de uma construção de API
##### Basic model of an API build

2. [MODELS](https://github.com/uadson/to-do-list-drf/blob/main/core/models.py)


		from django.db import models


		class Base(models.Model):
			created = models.DateTimeField(auto_now_add=True)
			modified = models.DateTimeField(auto_now=True)

			class Meta:
				abstract = True


		class Todo(Base):
			name = models.CharField(max_length=120)
			done = models.BooleanField(default=False)


3. [SERIALIZERS](https://github.com/uadson/to-do-list-drf/blob/main/core/serializers.py)]


		from core.models import Todo

		from rest_framework import serializers


		class TodoSerializer(serializers.ModelSerializer):
			class Meta:
				model = Todo
				fields = '__all__'


4. [VIEWS](https://github.com/uadson/to-do-list-drf/blob/main/core/views/home_view.py)



		from core.models import Todo
		from core.serializers import TodoSerializer

Function Based Views e Class Based Views
		from rest_framework.decorators import api_view
		from rest_framework.exceptions import NotFound
		from rest_framework.response import Response
		from rest_framework import status

Class Based Views
		from rest_framework.views import APIView
		from rest_framework import generics

ModelViewSets
		from rest_framework import viewsets


### Class Based View

		class TodoListAndCreate(APIView):

		    def get(self, request):
		        todo = Todo.objects.all()
		        serializer = TodoSerializer(todo, many=True)
		        return Response(serializer.data)

		    def post(self, request):
		        serializer = TodoSerializer(data=request.data)
		        if serializer.is_valid():
		            serializer.save()
		            return Response(serializer.data, status=status.HTTP_201_CREATED)
		        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


		class TodoDetailChangeAndDelete(APIView):

		    def get_object(self, pk):
		        try:
		            return Todo.objects.get(pk=pk)
		        except Todo.DoesNotExist:
		            raise NotFound()

		    def get(self, request, pk):
		        todo = self.get_object(pk)
		        serializer = TodoSerializer(todo)
		        return Response(serializer.data)

		    def put(self, request, pk):
		        todo = self.get_object(pk)
		        serializer = TodoSerializer(todo, data=request.data)
		        if serializer.is_valid():
		            serializer.save()
		            return Response(serializer.data)
		        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		    def delete(self, request, pk):
		        todo = self.get_object(pk)
		        todo.delete()
		        return Response(status=status.HTTP_204_NO_CONTENT)

#### OU

### Function Based View

		@api_view(['GET', 'POST'])
		def todo_list(request):
		   if request.method == 'GET':
		       todo = Todo.objects.all()
		       serializer = TodoSerializer(todo, many=True)
		       return Response(serializer.data)
		   elif request.method == 'POST':
		       serializer = TodoSerializer(data=request.data)
		       if serializer.is_valid():
		           serializer.save()
		           return Response(serializer.data, status=status.HTTP_201_CREATED)
		       return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


		@api_view(['GET', 'PUT', 'DELETE'])
		def todo_detail_change_and_delete(request, pk):
		   try:
		       todo = Todo.objects.get(pk=pk)
		   except Todo.DoesNotExist:
		       return Response(status=status.HTTP_404_NOT_FOUND)

		   if request.method == 'GET':
		       serializer = TodoSerializer(todo)
		       return Response(serializer.data)
		   elif request.method == 'PUT':
		       serializer = TodoSerializer(todo, data=request.data)
		       if serializer.is_valid():
		           serializer.save()
		           return Response(serializer.data)
		       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		   elif request.method == 'DELETE':
		       todo.delete()
		       return Response(status=status.HTTP_204_NO_CONTENT)


### "Classes Genéricas"

		class TodoListAndCreate(generics.ListCreateAPIView):
		    queryset = Todo.objects.all()
		    serializer_class = TodoSerializer


		class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
		    queryset = Todo.objects.all()
		    serializer_class = TodoSerializer


### Model ViewSets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


5. [URLS](https://github.com/uadson/to-do-list-drf/blob/main/core/urls/home_url.py)


		from django.urls import path

		# Class Based View
		from core.views.home_view import TodoListAndCreate, TodoDetailChangeAndDelete

		# Function Based View
		from core.views.home_view import todo_list, todo_detail_change_and_delete

		# Model View Set

		from core.views.home_view import TodoViewSet
		from rest_framework.routers import DefaultRouter


		app_name = 'core'

		urlpatterns = [
		    # with Class Based View

		    path('', TodoListAndCreate.as_view(), name='todo_list'),
		    path('<int:pk>/', TodoDetailChangeAndDelete.as_view(), name='detail_change_delete'),

		    # with Function Based View

		    path('', todo_list, name='todo_list'),
		    path('<int:pk>/', todo_detail_change_and_delete, name='detail_change_delete'),
		]


		# Model View Set
		
		router = DefaultRouter()
		router.register(r'', TodoViewSet)
		urlpatterns = router.urls