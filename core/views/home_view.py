from django.shortcuts import HttpResponse

from django.views.generic import View


class TestView(View):
    def get(*args, **kwargs):
        return HttpResponse('Hello Dev')
