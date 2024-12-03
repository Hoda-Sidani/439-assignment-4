import csv
from django.core.management.base import BaseCommand
from myapp3.models import Contact

class Command(BaseCommand):
    help = "Import contacts from CSV"

    def handle(self, *args, **kwargs):
        with open('data/contacts.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Contact.objects.create(
                    name=row['Person'],
                    speciality=row['Job Title'],
                    fees=float(row['Fees'].replace('$', '').replace(',', '')),
                    contact_info=row['Contact Info'],
                    address=row['Address'],
                    recommendation=int(row['Recommendation']),
                    gender=row['Gender'],  # Correctly assign Gender from CSV
                    hospital=row['Hospital'],  # Correctly assign Hospital from CSV
                    email=row.get('Email', None),  # Correctly assign Email from CSV
                    experience=int(row['Experience'])  # Correctly assign Experience from CSV
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported contacts'))
