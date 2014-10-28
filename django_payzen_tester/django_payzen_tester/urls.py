from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^payment/', include("django_payzen.urls")),
)
