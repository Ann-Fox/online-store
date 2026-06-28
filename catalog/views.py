from django.shortcuts import render
from catalog.models import Product

def catalog_list_view(request):
    products = Product.objects.filter(is_active=True)
    # if request.user.is_authentificated and hasattr(request.user, 'customer__profile'):
        # products = Product.objects.select_related('teacher__user')
    context = {
        'products': products
    }

    return render(request, 'catalog_list.html', context)