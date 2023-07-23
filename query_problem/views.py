from django.shortcuts import render, HttpResponse
from django.db import connection
from django.db import reset_queries
from .models import Album


def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func()
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return results

    return inner_func


# # @database_debug
def check_query_performance(request):
    albums_qs = Album.objects.select_related('artist').all()
    for album in albums_qs:
        print("", album.name, "\n", album.artist.first_name, "\n", album.artist.country.name)
    context = {
        "Hello": 12
    }
    return HttpResponse(context)

