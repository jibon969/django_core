from django.contrib import admin
from .models import Comment, Replay


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'blog', 'approve', 'created_at', 'updated_at']
    list_editable = ['approve']
    search_fields = ['name', 'email', 'body']


@admin.register(Replay)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ['comment', 'body', 'approve', 'created_at']
    list_editable = ['approve']
    search_fields = ['body']
