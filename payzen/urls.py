# pylint: disable=C0103, E1120
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^payment/', include("django_payzen.urls")),
)
