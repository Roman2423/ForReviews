from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ReviewForm

def product_list(request):
    """Отображает список всех продуктов с ссылками на страницу деталей."""
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    """
    Отображает детали выбранного продукта:
    - данные продукта,
    - форму для добавления отзыва,
    - список уже добавленных отзывов.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()  

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)

