"""
URL configuration for config project.
"""
import os
import logging
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

logger = logging.getLogger(__name__)


def serve_media(request, path):
    """Serve media files in production. Tries multiple paths."""
    from django.http import Http404, HttpResponseServerError
    from pathlib import Path

    # All possible paths where media might be stored
    paths_to_try = [
        settings.MEDIA_ROOT,
        '/app/medias',
        '/data/medias',
        '/medias',
        '/app/data/medias',
    ]

    # Log what we're looking for
    logger.error(f"[MEDIA] Looking for: {path}")
    logger.error(f"[MEDIA] MEDIA_ROOT setting: {settings.MEDIA_ROOT}")

    # Check all paths
    for root in paths_to_try:
        full_path = Path(root) / path if root else None
        if full_path and full_path.exists():
            logger.error(f"[MEDIA] FOUND at: {full_path}")
            return serve(request, path, document_root=root)
        elif full_path:
            logger.error(f"[MEDIA] Not found: {full_path}")

    # Final fallback: list what's in /app and /data
    for p in ['/app', '/data', '/medias']:
        if Path(p).exists():
            try:
                contents = list(Path(p).iterdir())[:10]
                logger.error(f"[MEDIA] Contents of {p}: {[c.name for c in contents]}")
            except Exception as e:
                logger.error(f"[MEDIA] Error listing {p}: {e}")

    raise Http404(f"Media file not found: {path}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

# Always serve media files (works in both DEBUG and production)
urlpatterns += [
    re_path(r'^medias/(?P<path>.*)$', serve_media),
]

# Also add static files for production
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]