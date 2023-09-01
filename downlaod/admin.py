from django.contrib import admin
import csv
from io import StringIO
from django.core.paginator import Paginator
from django.http import StreamingHttpResponse
from .models import Student

admin.site.register(Student)


def export_as_csv_action(description="Export selected objects as CSV file", header=True):
    def export_as_csv(modeladmin, request, queryset):

        def chunked_iterator(queryset, chunk_size=1000):
            paginator = Paginator(queryset, chunk_size)
            for page in range(1, paginator.num_pages + 1):
                for obj in paginator.page(page).object_list:
                    yield obj

        queryset = chunked_iterator(queryset)

        def row_generator(queryset):

            csvfile = StringIO()
            csvwriter = csv.writer(csvfile)

            def read_and_flush():
                csvfile.seek(0)
                data = csvfile.read()
                csvfile.seek(0)
                csvfile.truncate()
                return data

            header = False

            if not header:
                header = True
                csvwriter.writerow(['title', 'dept', 'roll'])
                data = read_and_flush()
                yield data

            for obj in queryset:
                csvwriter.writerow([obj.email, obj.last_name])  # your data here

                data = read_and_flush()
                yield data

        response = StreamingHttpResponse(row_generator(queryset), content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % 'yourfilename'

        return response

    export_as_csv.short_description = description
    return export_as_csv
