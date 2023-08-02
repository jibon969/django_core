from django import forms
from django.forms import Textarea
from .models import Blog, Category, Comment, Reply


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
        ]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'category',
            'image',
            'description',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'approve']

        # Override the Customer some fields
        widgets = {
            'body': Textarea(attrs={'rows': 3, 'cols': 3}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'body']