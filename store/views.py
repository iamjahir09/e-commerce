from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CheckoutForm, SignUpForm
from .models import Category, Order, OrderItem, Product

def product_list(request):
    products = Product.objects.filter(available=True, stock__gt=0).select_related("category")
    query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "").strip()
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, "store/product_list.html", {
        "products": products.distinct(),
        "categories": Category.objects.all(),
        "query": query,
        "selected_category": category_slug,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, "store/product_detail.html", {"product": product})

def signup(request):
    if request.user.is_authenticated:
        return redirect("product_list")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("product_list")
    return render(request, "store/signup.html", {"form": form})

def cart_detail(request):
    cart = Cart(request)
    return render(request, "store/cart.html", {"items": list(cart.items()), "total": cart.total()})

@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    if product.stock < 1:
        messages.error(request, "This product is out of stock.")
    else:
        quantity = max(1, int(request.POST.get("quantity", 1)))
        Cart(request).add(product, quantity)
        messages.success(request, f"{product.name} added to your cart.")
    return redirect(request.POST.get("next") or "cart_detail")

@require_POST
def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Cart(request).remove(product)
    messages.success(request, "Product removed from your cart.")
    return redirect("cart_detail")

@login_required
def checkout(request):
    cart = Cart(request)
    items = list(cart.items())
    if not items:
        messages.error(request, "Your cart is empty.")
        return redirect("product_list")
    initial = {"full_name": request.user.get_full_name() or request.user.username, "email": request.user.email}
    form = CheckoutForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            current_items = list(cart.items())
            if not current_items:
                messages.error(request, "Your cart is empty.")
                return redirect("cart_detail")
            for item in current_items:
                product = Product.objects.select_for_update().get(pk=item["product"].pk)
                if product.stock < item["quantity"] or not product.available:
                    messages.error(request, f"Not enough stock for {product.name}. Please update your cart.")
                    return redirect("cart_detail")
            total = sum((item["subtotal"] for item in current_items), start=0)
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data["full_name"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                city=form.cleaned_data["city"],
                postal_code=form.cleaned_data["postal_code"],
                total=total,
            )
            for item in current_items:
                product = Product.objects.get(pk=item["product"].pk)
                OrderItem.objects.create(order=order, product=product, product_name=product.name, price=product.price, quantity=item["quantity"])
                product.stock -= item["quantity"]
                product.save(update_fields=["stock"])
            cart.clear()
        messages.success(request, f"Order #{order.pk} placed successfully.")
        return redirect("order_detail", order_id=order.pk)
    return render(request, "store/checkout.html", {"form": form, "items": items, "total": cart.total()})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "store/order_history.html", {"orders": orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "store/order_detail.html", {"order": order})
