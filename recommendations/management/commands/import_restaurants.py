from django.core.management.base import BaseCommand
from recommendations.models import Restaurant
import csv

class Command(BaseCommand):
    help = 'Imports restaurants from a specified CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file_path']

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if your CSV has one
            for row in reader:
                _, created = Restaurant.objects.get_or_create(
                    name=row[1],  # Assuming the second column is the restaurant name
                    category=row[0],  # Assuming the first column is the category
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported restaurant "{row[1]}"'))  # Corrected to row[1] for the restaurant name
