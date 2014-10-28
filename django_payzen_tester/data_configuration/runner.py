from django.core import management
from django.test import runner


class DjangoPayzenTestSuiteRunner(runner.DiscoverRunner):

    def setup_databases(self, **kwargs):
        data_struct = super(DjangoPayzenTestSuiteRunner, self).setup_databases(
            **kwargs)
        management.call_command("load_site")
        return data_struct
