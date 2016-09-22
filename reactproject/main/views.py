# from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

# Create your views here.


class IndexPageView(TemplateView):
    def get_context_data(self, request=None, **kwargs):
        context = {'value': 'valor'}
        return context

    def get(self, request):
        context = self.get_context_data(request)
        return TemplateResponse(request, template="test.html", context=context)
