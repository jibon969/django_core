from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['message']

    class Meta:
        model = Notification


admin.site.register(Notification, NotificationAdmin)
