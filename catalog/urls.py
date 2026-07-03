from django.urls import path
from .views import (
    catalog_list_view,
    product_create_view,
    CatalogListView,
    ProductDetailView,
)

urlpatterns = [
    path("", CatalogListView.as_view(), name="home"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/create", product_create_view, name="product-create"),
]
