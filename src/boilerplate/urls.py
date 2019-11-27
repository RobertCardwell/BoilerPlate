from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    # home is referencing the dummy placeholder function, for testing
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
  