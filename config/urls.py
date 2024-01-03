from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.urls import include, path

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/dron/', include('apps.dron.urls')),
                  path('api/core/', include('apps.core.urls')),
                  re_path(r'^data/(?P<path>.*)/$', serve, {'document_root': settings.FILES_ROOT}),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

