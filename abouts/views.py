import asyncio
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "templates/abouts/abouts.html"

class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")
