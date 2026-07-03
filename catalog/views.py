from django.shortcuts import redirect, render
from catalog.forms import ProductForm, ProductImageFormSet
from catalog.models import Category, Product
from shop.forms_utils import apply_bootstrap_classes
from django.views.generic import ListView


def catalog_list_view(request):
    products = Product.objects.filter(is_active=True)
    # if request.user.is_authentificated and hasattr(request.user, 'customer__profile'):
    # products = Product.objects.select_related('teacher__user')
    context = {"products": products}

    return render(request, "catalog_list.html", context)


class CatalogListView(ListView):
    model = Product
    template_name = "catalog_list.html"
    context_object_name = "products"

    def get_queryset(self):
        products = Product.objects.filter(is_active=True)
        category_slug = self.request.GET.get("category")

        if category_slug:
            products = products.filter(category__slug=category_slug)

        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        context['selected_category'] = self.request.GET.get('category', '')
        return context







def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        formset = ProductImageFormSet(
            request.POST, request.FILES, instance=None
        )  # для нового товара instance=None

        apply_bootstrap_classes(form)
        for image_form in formset:
            apply_bootstrap_classes(image_form)

        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product  # привязываем product к formset
            formset.save()  # сохраняем изображения
            return redirect("home")  # перенаправляем на каталог
    else:
        form = ProductForm(initial={"is_active": True})
        formset = ProductImageFormSet()

        apply_bootstrap_classes(form)
        for image_form in formset:
            apply_bootstrap_classes(image_form)

    return render(
        request,
        "product_form.html",
        {
            "form": form,
            "formset": formset,
        },
    )
