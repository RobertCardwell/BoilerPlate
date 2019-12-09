from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import home

urlpatterns = [
    # home is referencing the dummy placeholder function, for testing
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
