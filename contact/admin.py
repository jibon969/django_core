from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    class Mata:
        model = Contact
        list_per_page = 20
        list_editable = ('phone', 'email',)


admin.site.register(Contact)
