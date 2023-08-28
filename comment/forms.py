from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Text goes here', 'rows': '4', 'cols': '10'}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ReplayForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Text goes here', 'rows': '4', 'cols': '10'}))

    class Meta:
        model = Replay
        fields = [
            'comment',
            'body',
            'approve'
        ]


class ApproveCommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'approve'
        ]
