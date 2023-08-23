# movies/views.py
from django.http import HttpResponse
import time
from .models import Movies, Theatres
from asgiref.sync import sync_to_async
import asyncio


def get_movies():
    print("getting movies ....")
    time.sleep(2)
    qs = Movies.objects.all()
    print(qs)
    print("all movies fetched")


def get_theatres():
    print("getting theatres ...")
    time.sleep(5)
    qs = Theatres.objects.all()
    print(qs)
    print("all theatres fetched")


@sync_to_async
def get_movies_async():
    print("getting movies ....")
    time.sleep(2)
    qs = Movies.objects.all()
    print(qs)
    print("all movies fetched")


@sync_to_async
def get_theatres_async():
    print("getting theatres ...")
    time.sleep(5)
    qs = Theatres.objects.all()
    print(qs)
    print("all theatres fetched")


def sync_view(request):
    start_time = time.time()
    get_movies()
    get_theatres()
    total = time.time() - start_time
    return HttpResponse(f"time taken {total}")


async def async_view(request):
    start_time = time.time()
    # approach 1
    # movie_task = asyncio.ensure_future(get_movies_async())
    # theatre_task = asyncio.ensure_future(get_theatres_async())
    # await asyncio.wait([movie_task, theatre_task])
    # approach 2 using gather
    await asyncio.gather(get_movies_async(), get_theatres_async())
    total = time.time() - start_time
    return HttpResponse(f"time taken async {total}")
