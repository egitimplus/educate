from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^components/', include('components.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^library/', include('library.urls')),
    url(r'^curricula/', include('curricula.urls')),
    url(r'^publishers/', include('publishers.urls')),
    url(r'^auth/', include('users.urls')),
    url(r'^categories/', include('educategories.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^tests/', include('tests.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
