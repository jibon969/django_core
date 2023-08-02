from django.http import HttpResponse
import csv


# Students name
NAME = ['Jibon', 'Payel', 'Sakib']
# QUIZ Subject
SUBJECT = ['Math', 'Programming', 'Database', 'Problem-Solving']


def download_csv(request):
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=student.csv'
    writer = csv.writer(response)
    writer.writerow(['id', 'Student Name', 'Dept', 'Roll'])
    for (name, sub) in zip(NAME, SUBJECT):
        writer.writerow([name, sub])
    return response


