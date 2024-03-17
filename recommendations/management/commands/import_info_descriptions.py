import csv
from django.core.management.base import BaseCommand
from recommendations.models import Restaurant

class Command(BaseCommand):
    help = 'Import restaurant data from CSV and mark curated restaurants'

    def handle(self, *args, **options):
        # First, read the curated restaurant names
        with open('data/category_restaurants_list.csv', mode='r', encoding='utf-8') as curated_file:
            curated_reader = csv.DictReader(curated_file)
            curated_names = [row['Restaurant A'] for row in curated_reader]

        # Then, import restaurant info and mark as curated if in the curated list
        with open('data/restaurant_info_descriptions.csv', mode='r', encoding='utf-8') as descriptions_file:
            descriptions_reader = csv.DictReader(descriptions_file)
            for row in descriptions_reader:
                # Check if the restaurant is in the curated list
                is_curated = row['name'] in curated_names
                Restaurant.objects.update_or_create(
                    index_name=row['index'],
                    defaults={
                        'name': row['name'],
                        'address': row['address'],
                        'phone': row['phone'],
                        'website': row['website'],
                        'description': row['description'],
                        'is_curated': is_curated  # Set the is_curated flag
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported restaurant data and marked curated restaurants.'))
