from django.urls import path
from .views import catalog_list_view, product_create_view, CatalogListView

urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    path('products/create', product_create_view, name='product-create'),
]
