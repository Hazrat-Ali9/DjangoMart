from django.shortcuts import render
from store.models import Product, Category
from cart.models import CartItem

def home(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    # cart_items_count = CartItem.objects.filter(user=request.user).count()
    # print("cart_items_count: ", cart_items_count)
    return render(request, 'index.html', {'products': products, 'categories': categories, })