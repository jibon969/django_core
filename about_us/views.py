from django.shortcuts import render
from htmlmin.decorators import minified_response
from .models import (
    AboutInfo,
    SecurityPrivacy,
    ReturnPolicy,
    TermsConditions,
    MoneyRefund,
    DeliveryPayment,
    YoutubeVideo,
    HelpCenter
)


@minified_response
def about_us(request):
    """
    Renders the about page.

    This function retrieves the title and description from the AboutInfo model
    and passes them as context to the 'about.html' template.

    URL: <base_url>/about-us/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """

    queryset = AboutInfo.objects.values('description').first()
    context = {
        'about_info': queryset,
    }
    return render(request, 'about_us/about.html', context)


@minified_response
def security_privacy(request):
    """
    Renders the security and privacy page.

    This function retrieves the description from the SecurityPrivacy model
    and passes it as context to the 'security-privacy.html' template.

    URL: <base_url>/privacy/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """

    queryset = SecurityPrivacy.objects.values('description').first()
    context = {
        'security_privacy': queryset,
    }
    return render(request, 'about_us/security-privacy.html', context)


@minified_response
def return_policy(request):
    """
    Renders the return policy page.

    This function retrieves the title and description from the ReturnPolicy model
    and passes them as context to the 'return-policy.html' template.

    URL: <base_url>/return-policy/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    queryset = ReturnPolicy.objects.values('description').first()
    context = {
        'return_policy': queryset,
    }
    return render(request, 'about_us/return-policy.html', context)


@minified_response
def terms_conditions(request):
    """
    Renders the terms and conditions page.

    This function retrieves the title and description from the TermsConditions model
    and passes them as context to the 'terms-and-conditions.html' template.

    URL: <base_url>/terms-conditions/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    queryset = TermsConditions.objects.values('description').first()
    context = {
        'terms_condition': queryset,
    }
    return render(request, 'about_us/terms-and-conditions.html', context)


@minified_response
def money_refund(request):
    """
    Renders the money refund page.

    This function retrieves the title and description from the MoneyRefund model
    and passes them as context to the 'money-refund.html' template.

    URL: <base_url>/money-refund/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    queryset = MoneyRefund.objects.values('description').first()
    context = {
        'money_refund': queryset
    }
    return render(request, 'about_us/money-refund.html', context)


@minified_response
def delivery_and_payment(request):
    """
    Renders the delivery and payment page.

    This function retrieves the title and description from the DeliveryPayment model
    and passes them as context to the 'delivery-and-payment.html' template.

    URL: <base_url>/delivery-and-payment/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    queryset = DeliveryPayment.objects.values('description').first()
    context = {
        'delivery_and_payment': queryset
    }
    return render(request, 'about_us/delivery-and-payment.html', context)


@minified_response
def how_to_buy(request):
    """
    Renders the YoutubeVideo page.

    This function retrieves the title and description from the YoutubeVideo model
    and passes them as context to the 'how-to-buy.html' template.

    URL: <base_url>/how-to-buy/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    videos = YoutubeVideo.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'about_us/how-to-buy.html', context)


@minified_response
def help_center(request):
    """
    Renders the HelpCenter page.

    This function retrieves the title and description from the HelpCenter model
    and passes them as context to the 'help-center.html' template.

    URL: <base_url>/help-center/
    Method: GET

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    queryset = HelpCenter.objects.values('description').first()
    context = {
        'help_center': queryset
    }
    return render(request, 'about_us/help-center.html', context)
