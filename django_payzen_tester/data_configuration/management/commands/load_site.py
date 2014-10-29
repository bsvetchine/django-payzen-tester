from django.core.management.base import BaseCommand

from django.contrib.sites.models import Site


class Command(BaseCommand):

    def handle(self, *args, **options):
        site = Site.objects.get_current()
        site.name = "ngrok url"
        site.domain = "django-payzen.ngrok.com"
        site.save()
