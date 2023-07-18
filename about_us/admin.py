from django.contrib import admin
from .models import (
    AboutInfo,
    SecurityPrivacy,
    TermsConditions,
    ReturnPolicy,
    MoneyRefund,
    DeliveryPayment,
    YoutubeVideo,
    HelpCenter
)


class AboutInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'timestamp']

    class Meta:
        model = AboutInfo


admin.site.register(AboutInfo, AboutInfoAdmin)


class SecurityPrivacyAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'timestamp']

    class Meta:
        model = SecurityPrivacy


admin.site.register(SecurityPrivacy, SecurityPrivacyAdmin)


class TermsConditionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    list_per_page = 20

    class Meta:
        model = TermsConditions


admin.site.register(TermsConditions, TermsConditionsAdmin)


class ReturnPolicyAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'timestamp']

    class Meta:
        model = ReturnPolicy


admin.site.register(ReturnPolicy, ReturnPolicyAdmin)


class MoneyRefundAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    list_per_page = 20

    class Meta:
        model = MoneyRefund


admin.site.register(MoneyRefund, MoneyRefundAdmin)


class DeliveryPaymentAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    list_per_page = 20

    class Meta:
        model = DeliveryPayment


admin.site.register(DeliveryPayment, DeliveryPaymentAdmin)


# Here Register Youtube Video models
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'video', 'timestamp']

    class Meta:
        model: YoutubeVideo


admin.site.register(YoutubeVideo, YoutubeVideoAdmin)


class HelpCenterAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'timestamp']

    class Meta:
        model: HelpCenter


admin.site.register(HelpCenter, HelpCenterAdmin)