from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from courses.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('class/', include(('courses.urls', 'courses'), namespace='courses')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
