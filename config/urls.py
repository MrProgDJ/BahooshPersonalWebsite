"""
URL configuration for config project.
"""
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve


def serve_media(request, path, document_root=None):
    """Serve media files in production."""
    return serve(request, path, document_root=document_root)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

# Always serve media files (works in both DEBUG and production)
urlpatterns += [
    re_path(r'^medias/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Also add static files for production
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
