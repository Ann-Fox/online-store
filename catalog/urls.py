from django.urls import path
from .views import (
    CatalogListView,
    ProductCreateView,
    ProductListJSONView,
    ProductListFetchView,
)


urlpatterns = [
    path("", CatalogListView.as_view(), name="home"),
    path("products/create", ProductCreateView.as_view(), name="product-create"),
    path("products/product-json/", ProductListJSONView.as_view(), name="product-json"),
    path(
        "products/product-fetch/", ProductListFetchView.as_view(), name="product-fetch"
    ),
    # path("products/<slug:slug>/", ProductDetailView.as_view(), name="product-detail"),
]
