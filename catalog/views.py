from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

# Главная страница с продуктами
class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

# Страница с деталями продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# Страница контактов
class ContactView(TemplateView):
    template_name = 'catalog/contact.html'
