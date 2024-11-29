from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Показывать в админке id и название категории

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Показывать id, название, цену и категорию продукта
    list_filter = ('category',)  # Добавить фильтр по категории
    search_fields = ('name', 'description')  # Добавить поиск по названию и описанию
