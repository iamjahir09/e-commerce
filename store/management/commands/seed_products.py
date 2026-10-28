
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, Product


class Command(BaseCommand):
    help = "Add demo categories and products"

    def handle(self, *args, **options):
        products = [
            ("Electronics", "Wireless Headphones", "Wireless headphones with clear sound and comfortable ear cushions.", "1999.00", 25, "photo-1505740420928-5e560c06d30e"),
            ("Electronics", "Smart Watch", "Smart watch with activity tracking and everyday notifications.", "2499.00", 18, "photo-1523275335684-37898b6baf30"),
            ("Electronics", "Digital Camera", "Compact digital camera for travel, events and everyday photography.", "4599.00", 8, "photo-1516035069371-29a1b244cc32"),
            ("Electronics", "Bluetooth Speaker", "Portable speaker with rich sound for home and outdoor use.", "1299.00", 22, "photo-1608043152269-423dbba4e7e1"),
            ("Electronics", "Wireless Mouse", "Ergonomic wireless mouse for work, study and everyday browsing.", "599.00", 35, "photo-1527864550417-7fd91fc51a46"),
            ("Electronics", "Mechanical Keyboard", "Responsive keyboard designed for comfortable typing and gaming.", "2299.00", 14, "photo-1587829741301-dc798b83add3"),
            ("Electronics", "Laptop Backpack", "Padded backpack with dedicated storage for a laptop and accessories.", "1499.00", 20, "photo-1553062407-98eeb64c6a62"),
            ("Electronics", "USB-C Hub", "Compact multi-port hub for connecting essential devices.", "899.00", 30, "photo-1625842268584-8f3296236761"),
            ("Electronics", "Gaming Headset", "Over-ear gaming headset with a microphone and immersive sound.", "1899.00", 16, "photo-1599669454699-248893623440"),
            ("Electronics", "Portable SSD", "Compact solid-state drive for storing and transferring files.", "3499.00", 12, "photo-1597872200969-2b65d56bd16b"),
            ("Electronics", "Laptop Stand", "Adjustable stand for a comfortable laptop viewing position.", "799.00", 24, "photo-1527864550417-7fd91fc51a46"),
            ("Electronics", "Webcam", "USB webcam for online meetings, classes and video calls.", "1299.00", 19, "photo-1587826080692-f439cd0b70da"),
            ("Electronics", "Power Bank", "Portable power bank for charging compatible devices on the go.", "1199.00", 28, "photo-1609091839311-d5365f9ff1c5"),
            ("Electronics", "LED Monitor", "Desktop monitor designed for work, study and entertainment.", "7999.00", 7, "photo-1527443224154-c4a3942d3acf"),
            ("Electronics", "Wireless Charger", "Convenient wireless charging pad for compatible smartphones.", "999.00", 21, "photo-1591290619762-c588b7f4a1a2"),
            ("Electronics", "Gaming Controller", "Ergonomic controller for compatible gaming devices.", "1799.00", 15, "photo-1592840496694-26d035b52b48"),

            ("Mobiles", "Smartphone Stand", "Adjustable desktop stand for video calls and hands-free viewing.", "349.00", 40, "photo-1512499617640-c74ae3a79d37"),
            ("Mobiles", "Fast Charging Adapter", "Compact fast charging adapter for compatible mobile devices.", "799.00", 26, "photo-1583394838336-acd977736f90"),
            ("Mobiles", "Protective Phone Case", "Lightweight protective case with a comfortable grip.", "299.00", 50, "photo-1601593346740-925612772716"),
            ("Mobiles", "Wireless Earbuds", "Compact wireless earbuds for calls, music and daily commutes.", "1799.00", 24, "photo-1606220945770-b5b6c2c55bf1"),
            ("Mobiles", "Screen Protector", "Protective screen film for compatible smartphones.", "199.00", 45, "photo-1511707171634-5f897ff02aa9"),
            ("Mobiles", "Car Phone Holder", "Secure phone holder for convenient car navigation.", "499.00", 22, "photo-1512941937669-90a1b58e7e9c"),
            ("Mobiles", "Selfie Stick", "Portable selfie stick for photos and video recording.", "399.00", 30, "photo-1516035069371-29a1b244cc32"),
            ("Mobiles", "Mobile Ring Holder", "Compact phone grip for a more secure handheld experience.", "149.00", 60, "photo-1512499617640-c74ae3a79d37"),

            ("Fashion", "Classic Sneakers", "Everyday sneakers with a versatile design and comfortable fit.", "1799.00", 20, "photo-1542291026-7eec264c27ff"),
            ("Fashion", "Casual Backpack", "Roomy everyday backpack for commuting, college and travel.", "1299.00", 18, "photo-1553062407-98eeb64c6a62"),
            ("Fashion", "Running Shoes", "Lightweight running shoes for training and everyday activity.", "2199.00", 16, "photo-1542291026-7eec264c27ff"),
            ("Fashion", "Classic Sunglasses", "Timeless sunglasses for everyday outdoor wear.", "699.00", 28, "photo-1511499767150-a48a237f0083"),
            ("Fashion", "Everyday Wrist Watch", "A clean everyday watch with a simple, versatile design.", "1599.00", 14, "photo-1524805444758-089113d48a6d"),
            ("Fashion", "Canvas Tote Bag", "Reusable canvas tote bag for shopping, books and daily essentials.", "399.00", 32, "photo-1544816155-12df9643f363"),
            ("Fashion", "Classic Denim Jacket", "Versatile denim jacket for casual everyday outfits.", "1899.00", 13, "photo-1543076447-215ad9ba6923"),
            ("Fashion", "Cotton T-Shirt", "Comfortable cotton T-shirt for everyday casual wear.", "499.00", 35, "photo-1521572163474-6864f9cf17ab"),
            ("Fashion", "Slim Fit Jeans", "Classic slim-fit jeans suitable for everyday styling.", "1199.00", 24, "photo-1542272604-787c3835535d"),
            ("Fashion", "Casual Hoodie", "Soft hoodie for comfortable everyday layering.", "1099.00", 19, "photo-1556821840-3a63f95609a7"),
            ("Fashion", "Leather Belt", "Classic belt designed for everyday casual and formal outfits.", "449.00", 26, "photo-1624222247344-550fb8b7b7b0"),
            ("Fashion", "Baseball Cap", "Adjustable cap for casual outfits and outdoor activities.", "299.00", 31, "photo-1588850561407-ed78c282e89b"),
            ("Fashion", "Travel Duffel Bag", "Spacious duffel bag for gym sessions and short trips.", "1499.00", 17, "photo-1553062407-98eeb64c6a62"),
            ("Fashion", "Formal Shoes", "Classic formal footwear for office and special occasions.", "1999.00", 12, "photo-1614252369475-531eba835eb1"),

            ("Home", "Modern Table Lamp", "Minimal table lamp for a comfortable reading or work setup.", "899.00", 10, "photo-1507473885765-e6ed057f782c"),
            ("Home", "Ceramic Coffee Mug", "Durable ceramic mug for coffee, tea and everyday use.", "299.00", 30, "photo-1514228742587-6b1558fcca3d"),
            ("Home", "Insulated Water Bottle", "Reusable bottle designed to keep drinks ready throughout the day.", "549.00", 34, "photo-1602143407151-7111542de6e8"),
            ("Home", "Desk Organizer", "Keep stationery and small desk accessories neatly arranged.", "449.00", 21, "photo-1498050108023-c5249f4df085"),
            ("Home", "Throw Cushion", "Soft decorative cushion for sofas, chairs and bedroom spaces.", "599.00", 17, "photo-1584100936595-c0654b55a2e2"),
            ("Home", "Storage Basket", "Simple storage basket for organizing household essentials.", "399.00", 25, "photo-1593085260707-5377ba37f868"),
            ("Home", "Ceramic Flower Vase", "Decorative vase for flowers and modern home interiors.", "699.00", 15, "photo-1578500494198-246f612d3b3d"),
            ("Home", "Wall Clock", "Simple wall clock for living rooms, bedrooms and offices.", "799.00", 18, "photo-1563861826100-9cb868fdbe1c"),
            ("Home", "Bedsheet Set", "Comfortable bedsheet set for everyday bedroom use.", "1299.00", 14, "photo-1631049307264-da0ec9d70304"),
            ("Home", "Laundry Basket", "Practical basket for organizing laundry at home.", "599.00", 20, "photo-1631679706909-1844bbd07221"),
            ("Home", "Non-Stick Frying Pan", "Everyday frying pan for convenient home cooking.", "899.00", 16, "photo-1584990347449-a6e6a4e1e4f0"),
            ("Home", "Kitchen Storage Jars", "Storage jars for keeping kitchen ingredients organized.", "499.00", 27, "photo-1495521821757-a1efb6729352"),
            ("Home", "Floor Mat", "Practical floor mat for entryways and indoor spaces.", "349.00", 33, "photo-1600210492486-724fe5c67fb0"),
            ("Home", "Decorative Wall Art", "Decorative artwork for refreshing home interiors.", "999.00", 11, "photo-1579783902614-a3fb3927b6a5"),

            ("Beauty", "Skincare Travel Kit", "A compact travel pouch for organizing personal care essentials.", "699.00", 19, "photo-1608248543803-ba4f8c70ae0b"),
            ("Beauty", "Makeup Brush Set", "Everyday brush set for smooth and convenient makeup application.", "499.00", 23, "photo-1522335789203-aabd1fc54bc9"),
            ("Beauty", "Personal Care Kit", "A handy personal care kit for home or travel use.", "849.00", 15, "photo-1556229010-6c3f2c9ca5f8"),
            ("Beauty", "Face Moisturizer", "Daily moisturizer for a comfortable skincare routine.", "399.00", 25, "photo-1608248543803-ba4f8c70ae0b"),
            ("Beauty", "Sunscreen SPF 50", "Daily sunscreen for outdoor skincare protection.", "499.00", 30, "photo-1556229010-6c3f2c9ca5f8"),
            ("Beauty", "Face Cleanser", "Gentle facial cleanser for everyday skincare.", "299.00", 28, "photo-1556229010-6c3f2c9ca5f8"),
            ("Beauty", "Lip Balm Set", "Lip balm set for everyday lip care.", "199.00", 35, "photo-1608248543803-ba4f8c70ae0b"),
            ("Beauty", "Perfume", "Everyday fragrance for personal use and gifting.", "999.00", 17, "photo-1541643600914-78b084683601"),
            ("Beauty", "Hair Dryer", "Compact hair dryer for convenient home styling.", "1299.00", 12, "photo-1522337360788-8b13dee7a37e"),
            ("Beauty", "Electric Trimmer", "Personal grooming trimmer for everyday use.", "999.00", 14, "photo-1621607512214-68297480165e"),

            ("Sports", "Yoga Mat", "Comfortable exercise mat for stretching, yoga and home workouts.", "999.00", 20, "photo-1592432678016-e910b452f9a2"),
            ("Sports", "Fitness Dumbbells", "Compact dumbbells for strength training at home.", "1199.00", 12, "photo-1517836357463-d25dfeac3438"),
            ("Sports", "Sports Water Bottle", "Lightweight bottle for workouts, sports and outdoor activities.", "349.00", 30, "photo-1523362628745-0c100150b6bc"),
            ("Sports", "Football", "Durable football for recreational play and training.", "699.00", 18, "photo-1614632537423-1e6c2e7e0e4a"),
            ("Sports", "Badminton Racket", "Lightweight racket for recreational badminton matches.", "899.00", 16, "photo-1626224583764-f87db24ac4ea"),
            ("Sports", "Skipping Rope", "Fitness skipping rope for cardio and workout routines.", "249.00", 32, "photo-1517836357463-d25dfeac3438"),
            ("Sports", "Resistance Bands", "Versatile resistance bands for strength and mobility training.", "399.00", 25, "photo-1599058945522-28d584b6f0ff"),
            ("Sports", "Gym Gloves", "Workout gloves designed for a comfortable grip during training.", "499.00", 19, "photo-1534438327276-14e5300c3a48"),
            ("Sports", "Cricket Bat", "Recreational cricket bat for practice and casual matches.", "1499.00", 10, "photo-1531415074968-036ba1b575da"),
            ("Sports", "Sports Gym Bag", "Spacious bag for carrying gym clothes and training accessories.", "999.00", 15, "photo-1553062407-98eeb64c6a62"),

            ("Accessories", "Classic Wallet", "Slim wallet with practical storage for cards and cash.", "499.00", 22, "photo-1627123424574-724758594e93"),
            ("Accessories", "Travel Organizer", "Organizer pouch for cables, chargers and small travel items.", "599.00", 19, "photo-1553062407-98eeb64c6a62"),
            ("Accessories", "Leather Keychain", "Compact keychain for organizing everyday keys.", "199.00", 35, "photo-1511499767150-a48a237f0083"),
            ("Accessories", "Card Holder", "Slim card holder for carrying essential cards.", "299.00", 28, "photo-1627123424574-724758594e93"),
            ("Accessories", "Laptop Sleeve", "Protective sleeve for carrying a laptop during travel.", "699.00", 20, "photo-1593642632823-8f785ba67e45"),
            ("Accessories", "Travel Neck Pillow", "Supportive neck pillow for comfortable journeys.", "499.00", 17, "photo-1500530855697-b586d89ba3ee"),
            ("Accessories", "Key Organizer", "Compact accessory for keeping keys neatly arranged.", "249.00", 26, "photo-1511499767150-a48a237f0083"),
            ("Accessories", "Minimalist Bracelet", "Simple bracelet for everyday styling.", "349.00", 24, "photo-1611591437281-460bfbe1220a"),
            ("Accessories", "Compact Umbrella", "Portable umbrella for everyday travel and rainy weather.", "599.00", 21, "photo-1534274988757-a28bf1a57c17"),
            ("Accessories", "Reusable Shopping Bag", "Foldable reusable bag for shopping and daily errands.", "199.00", 40, "photo-1544816155-12df9643f363"),
        ]

        for category_name, name, description, price, stock, image_id in products:
            category, _ = Category.objects.get_or_create(
                slug=slugify(category_name),
                defaults={"name": category_name},
            )
            Product.objects.update_or_create(
                slug=slugify(name),
                defaults={
                    "category": category,
                    "name": name,
                    "description": description,
                    "price": price,
                    "stock": stock,
                    "image_url": f"https://images.unsplash.com/{image_id}?auto=format&fit=crop&w=800&q=80",
                    "available": True,
                },
            )

        self.stdout.write(self.style.SUCCESS(f"Demo data ready: {len(products)} products processed."))
