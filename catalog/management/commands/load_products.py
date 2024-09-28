from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загрузить тестовые продукты'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()  # Очистить все продукты
        category = Category.objects.get(name='Электроника')
        Product.objects.create(name='Смартфон', description='Смартфон с камерой', category=category, price=1000)
        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены'))
