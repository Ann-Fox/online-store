from django.urls import path
from .views import CatalogListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path("", CatalogListView.as_view(), name="home"),
    path("products/create", ProductCreateView.as_view(), name="product-create"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
]
