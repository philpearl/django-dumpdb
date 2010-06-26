from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        from django_dumpdb.dumprestore import load
        load()
