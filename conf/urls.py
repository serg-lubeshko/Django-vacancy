from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from vacancy.handler import custom_handler404, custom_handler400, custom_handler403, custom_handler500

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('vacancy.urls')),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
