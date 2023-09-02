from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

# from blog.sitemaps import PostSitemap

# sitemaps = {
#     'posts': PostSitemap,
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('', include('contact.urls')),
    path('', include('dynamic_slider.urls')),
    path('', include('notifications.urls')),
    path('', include('django_form.urls')),
    path('', include('about_us.urls')),
    path('', include('downlaod.urls')),
    path('', include('asynchronous.urls')),
    path('', include('blog.urls', namespace="blog")),

    # path('blog/', include('blog.urls', namespace='blog')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #      name='django.contrib.sitemaps.views.sitemap'),

]
