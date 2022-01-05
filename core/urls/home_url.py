from django.urls import path

from core.views.home_view import TestView


app_name = 'core'

urlpatterns = [
    path('', TestView.as_view(), name='teste')
]
