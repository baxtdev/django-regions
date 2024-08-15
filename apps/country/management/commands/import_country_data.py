# your_app/management/commands/import_country_data.py

import json
from django.core.management.base import BaseCommand
from apps.country.models import Country, Region, City

class Command(BaseCommand):
    help = 'Импортирует данные о странах, регионах и городах из JSON'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Путь к JSON файлу с данными о странах')

    def handle(self, *args, **options):
        json_file_path = options['json_file']
        
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        for country_data in data:
            country, created = Country.objects.get_or_create(
                name=country_data['name'],
                alpha2_code=country_data['iso2'],
                alpha3_code=country_data['iso3'],
            )
            
            for state_data in country_data.get('states', []):
                region, created = Region.objects.get_or_create(
                    name=state_data['name'],
                    country=country
                )
                
                for city_data in state_data.get('cities', []):
                    City.objects.get_or_create(
                        name=city_data['name'],
                        region=region
                    )

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы.'))
