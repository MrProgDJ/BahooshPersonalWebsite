"""
URL configuration for config project.
"""
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve


def serve_media(request, path, document_root=None):
    """Serve media files in production. Falls back to alternate paths."""
    from django.http import Http404
    from pathlib import Path

    # Try multiple potential paths
    paths_to_try = [
        document_root,
        '/app/medias',
        '/medias',
        '/data/medias',
    ]

    for root in paths_to_try:
        if root and Path(root, path).exists():
            return serve(request, path, document_root=root)

    raise Http404(f"Media file not found: {path}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

# Always serve media files (works in both DEBUG and production)
urlpatterns += [
    re_path(r'^medias/(?P<path>.*)$', serve_media, {'document_root': settings.MEDIA_ROOT}),
]

# Also add static files for production
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]