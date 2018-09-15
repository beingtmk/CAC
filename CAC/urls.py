from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from django.contrib import admin

# Wagtail
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    # path("", TemplateView.as_view(template_name="home_page.html"), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),

    # Wagtail
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
