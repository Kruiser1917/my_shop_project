from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contacts, name='contact'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]  # убедитесь, что здесь нет лишних скобок
