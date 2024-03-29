from django.contrib import admin
from .models import Contact, ReplayContact


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['subject', 'phone', 'email']
    list_editable = ('subject', 'phone', 'email',)

    class Mata:
        model = Contact


admin.site.register(Contact, ContactAdmin)


class ReplayContactAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['message']
    list_editable = ('message',)

    class Mata:
        model = ReplayContact


admin.site.register(ReplayContact, ReplayContactAdmin)
