from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from cart.views import _cart_id
from cart.models import Cart, CartItem
from django.contrib import messages


def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cart')
    return render(request, 'accounts/register.html', {'form':form})

def profile(request):
    cart_items_count = CartItem.objects.filter(user=request.user).count()
    context = {'cart_items_count': cart_items_count}
    return render(request, 'accounts/dashboard.html', context)

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    for item in cart_item:
                        item.user = user
                        item.save()
            except:
                pass
            login(request, user)
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
        
        # login hoye geche
        
        return redirect('cart')
    return render(request, 'accounts/signin.html')

def user_logout(request):
    logout(request)
    return redirect('login')