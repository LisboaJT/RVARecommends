from django.core.management.base import BaseCommand, CommandError
from recommendations.models import Restaurant


class Command(BaseCommand):
    help = 'Deletes all restaurants from the database'

    def handle(self, *args, **options):
        # Confirm before proceeding
        if input("Are you sure you want to delete all restaurants? This cannot be undone. Type 'yes' to continue: ") != 'yes':
            self.stdout.write(self.style.WARNING('Operation cancelled.'))
            return

        try:
            count = Restaurant.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count[0]} restaurant(s).'))
        except Exception as e:
            raise CommandError(f'Error deleting restaurants: {str(e)}')