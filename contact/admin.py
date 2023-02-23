from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_editable = ('subject', 'phone', 'email',)

    class Mata:
        model = Contact


admin.site.register(Contact)
