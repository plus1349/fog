from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.urls.conf import path


urlpatterns: list = [
    path("", site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
