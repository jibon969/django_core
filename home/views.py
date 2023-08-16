from django.shortcuts import render
from django.views.generic.base import TemplateView


def home(request):
    return render(request, "home/home.html")


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home. self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context
