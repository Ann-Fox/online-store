from django.shortcuts import redirect, render
from catalog.forms import ProductForm, ProductImageFormSet
from catalog.models import Product
from shop.forms_utils import apply_bootstrap_classes

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
        formset = ProductImageFormSet(request.POST, request.FILES, instance=None)  # для нового товара instance=None

        apply_bootstrap_classes(form)
        for image_form in formset:
            apply_bootstrap_classes(image_form)

        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product  # привязываем product к formset
            formset.save()  # сохраняем изображения
            return redirect('home')  # перенаправляем на каталог
    else:
        form = ProductForm(initial={'is_active': True})
        formset = ProductImageFormSet()

        apply_bootstrap_classes(form)
        for image_form in formset:
            apply_bootstrap_classes(image_form)
        
    return render(
        request,
        'product_form.html',
        {
            'form': form,
            'formset': formset,
        },
    )