from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    list_display_links = ['email']

    class Meta:
        model = User


admin.site.register(User)
