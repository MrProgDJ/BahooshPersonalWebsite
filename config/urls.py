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
    """Serve media files in production."""
    from django.http import Http404
    from pathlib import Path

    logger.error(f"[MEDIA] Looking for: {path}")
    logger.error(f"[MEDIA] MEDIA_ROOT setting: {settings.MEDIA_ROOT}")

    # Log /app/medias contents
    media_dir = Path('/app/medias')
    if media_dir.exists():
        try:
            contents = []
            for p in media_dir.rglob('*'):
                if p.is_file():
                    contents.append(str(p.relative_to(media_dir)))
                if len(contents) >= 20:
                    break
            logger.error(f"[MEDIA] /app/medias files: {contents}")
        except Exception as e:
            logger.error(f"[MEDIA] Error listing: {e}")

    # Try /app/medias directly (where Django writes)
    full_path = Path('/app/medias') / path
    if full_path.exists():
        return serve(request, path, document_root='/app/medias')

    raise Http404(f"Media file not found: {path}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

urlpatterns += [
    re_path(r'^medias/(?P<path>.*)$', serve_media),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]