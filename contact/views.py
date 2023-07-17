from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
import csv


def contact(request):
    """
    This function based view work for contact page
    urls : http://127.0.0.1:8000/contact-us/
    :param request:
    :return:
    """
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if form.errors:
        errors = form.errors
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'contact/contact.html', context)


# Create your views here.
def download_contact_csv(request):
    """
    :param request:
    :return: 
    """
    queryset = Contact.objects.order_by('-timestamp')
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Subject', 'Full Name', 'E-mail', 'Phone', 'Message'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.subject, q.name, q.email, '0' + q.phone, q.message
        ])
        writer.writerow(row[:])

    response['Content-Disposition'] = 'attachment; filename="contact.csv"'
    return response
