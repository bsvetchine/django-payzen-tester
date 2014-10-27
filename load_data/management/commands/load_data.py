from django.core.management.base import BaseCommand

from django.contrib.sites.models import Site


class Command(BaseCommand):

    """Command that populates db for testing purposes."""

    help = "Load data into the database"

    def handle(self, *args, **options):
        site = Site.objects.get()
        site.name = "ngrok url"
        site.domain = "4f1fa68a.ngrok.com"
        site.save()
 