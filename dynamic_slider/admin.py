from django.contrib import admin
from .models import Slider, SingleSlider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'extra_large_devices', 'value', 'url_field']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model: Slider


admin.site.register(Slider, SliderAdmin)


class SingleSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    search_fields = ['title']
    list_per_page = 10

    class Meta:
        model = SingleSlider


admin.site.register(SingleSlider, SingleSliderAdmin)

