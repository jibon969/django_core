from django.contrib import admin
from .models import MetaInfo


class MetaInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'id',  'timestamp']
    search_fields = ['title']
    list_per_page = 20

    class Meta:
        model = MetaInfo


admin.site.register(MetaInfo, MetaInfoAdmin)