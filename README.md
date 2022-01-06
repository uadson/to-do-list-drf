# to-do-list-drf
Getting Started in Building a Project with Django Rest Framework


[![Build Status](https://app.travis-ci.com/uadson/to-do-list-drf.svg?branch=main)](https://app.travis-ci.com/uadson/to-do-list-drf)    [![Updates](https://pyup.io/repos/github/uadson/to-do-list-drf/shield.svg)](https://pyup.io/repos/github/uadson/to-do-list-drf/)    [![Python 3](https://pyup.io/repos/github/uadson/to-do-list-drf/python-3-shield.svg)](https://pyup.io/repos/github/uadson/to-do-list-drf/)


1. Instalation

	pip install djangorestframework


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

		from rest_framework.decorators import api_view
		from rest_framework.response import Response
		from rest_framework import status


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


5. [URLS](https://github.com/uadson/to-do-list-drf/blob/main/core/urls/home_url.py)


		from django.urls import path

		from core.views.home_view import todo_list


		app_name = 'core'

		urlpatterns = [
		    path('', todo_list, name='todo_list')
		]