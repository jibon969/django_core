from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import ReplayForm
from django.http import HttpResponseRedirect
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from htmlmin.decorators import minified_response
from django.db.models import Q
from django.contrib import messages
from blog.models import Blog


def comment_replay_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = ReplayForm(request.POST)
        if form.is_valid():
            replay = form.save(commit=False)
            replay.comment = comment
            replay.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ReplayForm()
    replays = comment.replays.all()
    context = {
        'comment': comment,
        'replays': replays,
        'form': form,
        'comment_title': Comment.objects.values('id', 'body')
    }
    return render(request, 'comment/replay-comment.html', context)
