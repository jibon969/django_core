from django.shortcuts import render
from .models import Slider, SingleSlider


def dynamic_slider(request):
    slider_list = Slider.objects.all().order_by('value')[:10]
    slider_queryset = SingleSlider.objects.all()[:10]
    context = {
        'slider_list': slider_list,
        'slider': slider_queryset
    }
    return render(request, "dynamic_slider/dynamic_slider.html", context)
