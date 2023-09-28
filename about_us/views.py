from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def about_us(request):
    """
    Function based view
    """
    return render(request, "about_us/about-us.html")


class AboutUs(View):
    """
    Class based view
    """
    # def get(self, request):
    #     return render(request, "abouts/abouts.html")

    # or

    template_name = "abouts/abouts.html"

    def get(self, request):
        return render(request, self.template_name)


class AboutUsView(TemplateView):
    template_name = "about_us/about-us.html"
