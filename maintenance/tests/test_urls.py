try:
    from django.conf.urls import include, patterns, url
except ImportError:  # 1.3 fallback
    from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    "",
    (r"^admin/", include(admin.site.urls)),
)
