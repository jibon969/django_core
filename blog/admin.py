from django.contrib import admin
from .models import Post, Comment,  Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class ReplyAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'body', 'approve']
    search_fields = ['name']
    list_editable = ['approve']

    class Meta:
        model = Reply


admin.site.register(Reply, ReplyAdmin)