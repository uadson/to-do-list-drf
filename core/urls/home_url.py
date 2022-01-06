from django.urls import path

from core.views.home_view import todo_list


app_name = 'core'

urlpatterns = [
    path('', todo_list, name='todo_list')
]
