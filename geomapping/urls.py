from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls.i18n import i18n_patterns

admin.sites.AdminSite.site_header = 'Abu Dhabi'
admin.sites.AdminSite.site_title = 'Geo Mapping System'
admin.sites.AdminSite.index_title = 'Geo Coding Adminpanel'

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('mapping.urls')),
) 

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)