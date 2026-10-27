from decimal import Decimal
from .models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get("cart", {})

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def add(self, product, quantity=1, override=False):
        key = str(product.id)
        current = int(self.cart.get(key, 0))
        next_quantity = int(quantity) if override else current + int(quantity)
        if next_quantity <= 0:
            self.cart.pop(key, None)
        else:
            self.cart[key] = min(next_quantity, product.stock)
        self.save()

    def remove(self, product):
        self.cart.pop(str(product.id), None)
        self.save()

    def items(self):
        products = Product.objects.filter(id__in=self.cart.keys(), available=True)
        for product in products:
            quantity = int(self.cart.get(str(product.pk), 0))
            if quantity > 0:
                yield {"product": product, "quantity": quantity, "subtotal": product.price * quantity}

    def total(self):
        return sum((item["subtotal"] for item in self.items()), Decimal("0.00"))

    def clear(self):
        self.session["cart"] = {}
        self.cart = {}
        self.session.modified = True
