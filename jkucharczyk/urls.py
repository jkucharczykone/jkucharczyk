from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include('mainsite.urls', namespace='mainsite')),
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls', namespace='blog')),
    path('sitemap.xml',sitemap, {'sitemaps':sitemaps}, name='django.contrib.views.sitemap')
]
