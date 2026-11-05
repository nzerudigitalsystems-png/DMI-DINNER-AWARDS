from django.core.management import BaseCommand, call_command

from apps.awards.models import AwardCategory


class Command(BaseCommand):
    help = 'Load the default award categories if the database has none.'

    def handle(self, *args, **options):
        if AwardCategory.objects.exists():
            self.stdout.write('Award categories already exist; leaving them unchanged.')
            return

        call_command('loaddata', 'categories', verbosity=0)
        self.stdout.write(
            self.style.SUCCESS(
                f'Loaded {AwardCategory.objects.count()} default award categories.'
            )
        )
