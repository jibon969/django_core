from django import forms
from .models import Comment, Reply


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'body']