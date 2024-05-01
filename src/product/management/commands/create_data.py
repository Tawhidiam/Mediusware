import json
from django.utils.text import slugify
from django.core.management import BaseCommand
from product.models import Variant,Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(r'C:\Users\tawhi\Downloads\Mediusware\django-coding-test\src\django_coding_test.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)
        
            for item in data:
                Product.objects.create(
                    title= item['fields']['title'],
                    sku = item['fields']['title'],
                    description = item['fields']['description']
                )
