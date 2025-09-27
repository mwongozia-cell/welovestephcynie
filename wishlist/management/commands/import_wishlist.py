import csv
from django.core.management.base import BaseCommand
from wishlist.models import WishlistItem

class Command(BaseCommand):
    help = "Import wishlist items from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_path']
        created = 0

        WishlistItem.objects.all().delete()
        self.stdout.write(self.style.WARNING("Existing wishlist items deleted."))

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                WishlistItem.objects.create(
                    type=row.get('Type', '').strip(),
                    brand=row.get('Brand', '').strip(),
                    website=row.get('Website', '').strip(),
                    item=row.get('Item', '').strip(),
                    preference=row.get('Preference', '').strip()
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Fresh import complete: {created} items added."))
