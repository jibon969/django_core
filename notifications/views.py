from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from django.contrib import messages


def notification_list(request):
    """
    :param request:
    :return:
    """
    if request.user.is_authenticated and request.user.is_staff:
        notifications = Notification.objects.filter(user=request.user).order_by('-id')
        context = {
            'notifications': notifications
        }
        return render(request, 'notification/notification.html', context)
    else:
        messages.add_message(request, messages.WARNING, "Sorry currently you don't have permission to access this file")
        return redirect('home')


def delete_notification(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    obj = get_object_or_404(Notification, pk=id)
    obj.delete()
    messages.add_message(request, messages.WARNING, "Successfully delete notification !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
