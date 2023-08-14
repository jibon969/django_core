from django.shortcuts import render
from django.views import View


def about_us(request):
    """
    Function based view
    """
    return render(request, "about_us/about-us.html")


class AboutUs(View):
    """
    Class based view
    """
    def get(self, request):
        return render(request, "about_us/about-us.html")


