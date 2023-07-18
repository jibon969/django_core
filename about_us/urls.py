from django.urls import path
from . import views

urlpatterns = [
    path('help-center/', views.help_center, name="help-center"),
    path('money-refund/', views.money_refund, name="money-refund"),
    path('security-privacy/', views.security_privacy, name="security-privacy"),
    path('return-policy/', views.return_policy, name="return-policy"),
    path('terms-conditions/', views.terms_conditions, name="terms-conditions"),
    path('how-to-buy/', views.how_to_buy, name="how-to-buy"),
    path('delivery-and-payment/', views.delivery_and_payment,
         name="delivery-and-payment"),
]