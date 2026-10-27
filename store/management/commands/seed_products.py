
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, Product


class Command(BaseCommand):
    help = "Add demo categories and products"

    def handle(self, *args, **options):
        products = [
            {
                "category": "Electronics",
                "name": "Wireless Headphones",
                "description": "Comfortable wireless headphones with clear sound and long battery life.",
                "price": "1999.00",
                "stock": 15,
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700",
            },
            {
                "category": "Electronics",
                "name": "Smart Watch",
                "description": "A modern smartwatch for daily activity tracking and notifications.",
                "price": "2499.00",
                "stock": 12,
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700",
            },
            {
                "category": "Electronics",
                "name": "Wireless Camera",
                "description": "Compact camera for capturing everyday moments and travel photos.",
                "price": "4599.00",
                "stock": 8,
                "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=700",
            },
            {
                "category": "Fashion",
                "name": "Classic Sneakers",
                "description": "Versatile everyday sneakers designed for comfort and casual style.",
                "price": "1799.00",
                "stock": 20,
                "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700",
            },
            {
                "category": "Fashion",
                "name": "Everyday Backpack",
                "description": "A practical backpack with space for daily essentials and accessories.",
                "price": "1299.00",
                "stock": 18,
                "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700",
            },
            {
                "category": "Home",
                "name": "Modern Table Lamp",
                "description": "A minimal table lamp for a comfortable reading or work setup.",
                "price": "899.00",
                "stock": 10,
                "image_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700",
            },
            {
                "category": "Home",
                "name": "Coffee Mug",
                "description": "A stylish ceramic mug for coffee, tea and everyday use.",
                "price": "299.00",
                "stock": 30,
                "image_url": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=700",
            },
            {
                "category": "Accessories",
                "name": "Classic Wrist Watch",
                "description": "A timeless wristwatch suitable for everyday wear and special occasions.",
                "price": "1599.00",
                "stock": 14,
                "image_url": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=700",
            },
        ]

        for item in products:
            category_name = item["category"]
            category, _ = Category.objects.get_or_create(
                slug=slugify(category_name),
                defaults={"name": category_name},
            )

            Product.objects.update_or_create(
                slug=slugify(item["name"]),
                defaults={
                    "category": category,
                    "name": item["name"],
                    "description": item["description"],
                    "price": item["price"],
                    "stock": item["stock"],
                    "image_url": item["image_url"],
                    "available": True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Demo data ready: {len(products)} products processed."
            )
        )
