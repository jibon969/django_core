from django.contrib import admin
from .models import Category, Blog, Comment, Reply
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class YourModelAdmin(SummernoteModelAdmin):
    # Specify the fields you want to use Summernote for
    summernote_fields = ('description',)


class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'email', 'body', 'approve']
    list_editable = ['approve']
    search_fields = ['name', 'email']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'body', 'approve']
    search_fields = ['name']
    list_editable = ['approve']

    class Meta:
        model = Reply


admin.site.register(Reply, ReplyAdmin)