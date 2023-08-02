from django.contrib.sitemaps import Sitemap
from .models import Blog


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Blog.published.all()

    def lastmod(self, obj):
        return obj.updated
