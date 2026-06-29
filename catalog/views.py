from django.shortcuts import redirect, render
from catalog.forms import ProductForm
from catalog.models import Product

def catalog_list_view(request):
    products = Product.objects.filter(is_active=True)
    # if request.user.is_authentificated and hasattr(request.user, 'customer__profile'):
        # products = Product.objects.select_related('teacher__user')
    context = {
        'products': products
    }

    return render(request, 'catalog_list.html', context)


def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save(commit=False)
            form.save()  # сохраняем товар
            return redirect('home')  # перенаправляем на каталог
    else:
        form = ProductForm(initial={'is_active': True})

    return render(request, 'product_form.html', {'form': form})