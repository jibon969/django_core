from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import csv


# Create your views here.
def download_contact_csv(request):
    queryset = Contact.objects.all().order_by('-timestamp')[:500]
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
        'ID', 'Subject', 'Full Name', 'E-mail', 'Phone', 'Message'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.id, q.subject, q.name, q.email, '0'+q.phone, q.message
        ])
        writer.writerow(row[:])

    response['Content-Disposition'] = 'attachment; filename="contact.csv"'
    return response
