# NovaCart – E-Commerce Using Advanced Web Technology

**NovaCart** is a web-based e-commerce application developed using Python and Django. It provides a simple online shopping experience where users can browse products, search and filter categories, add items to a shopping cart, place demo orders, and view their order history.

The project demonstrates the use of modern web technologies to develop a responsive e-commerce website with user authentication, product management, session-based cart functionality, and order processing.

## Features

- **Product Catalogue:** Browse available products and view product details.
- **Search and Filtering:** Search for products and filter them by category.
- **User Authentication:** Register and log in to a customer account.
- **Shopping Cart:** Add products to a session-based cart.
- **Checkout:** Submit checkout details and create demo orders.
- **Order Management:** View order history and individual order details.
- **Inventory Management:** Automatically reduce product stock when an order is placed.
- **Admin Dashboard:** Manage products, categories, and orders through Django Admin.
- **Responsive UI:** Use the website on desktop and mobile screens.
- **Database Integration:** Store application data using SQLite.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework and application logic |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Client-side interactions |
| SQLite | Database |
| Django Admin | Administrative management |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
ecommerce_advanced_web/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── db.sqlite3                 # Local database, if generated
├── shopsite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── store/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── templates/
    ├── static/
    └── ...
```

*Note: The structure above is representative. Some files and folders may vary depending on the project version.*

## Requirements

- Python 3.10 or newer
- pip
- A web browser
- Internet connection only if product images are loaded from remote URLs

## Installation and Setup

### 1. Clone the Repository

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows CMD:**

```cmd
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations store
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the administrator username, email, and password.

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application should now be available at:

- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

Keep the terminal running while using the application.

## Initial Configuration

After starting the project for the first time:

1. Open the Django Admin Panel.
2. Log in using the superuser credentials created during setup.
3. Add product categories first, using simple slugs such as `electronics`, `fashion`, or `accessories`.
4. Add products, assign categories, and configure their prices, stock quantities, and availability.
5. Optionally provide a direct, publicly accessible image URL for each product.
6. Visit the homepage to test product browsing, search, category filtering, and product details.
7. Register a normal customer account to test the shopping cart, checkout, and order history.

## How It Works

1. Customers browse products and explore available categories.
2. They add products to a session-based shopping cart.
3. During checkout, they submit the required order details.
4. The application creates a demo order and updates the relevant stock quantities.
5. Customers can view their previous orders and order details.
6. Administrators manage products, categories, and orders through Django Admin.

## Database

NovaCart uses **SQLite** as its default database. Django models and migrations manage the application's database schema.

The local database file is generated during setup and is excluded from Git using `.gitignore`. After cloning the repository, run the migrations to create the required database tables and add products through the admin panel.

## Security and Production Considerations

This project is intended for learning and demonstration purposes. Before deploying it to production:

- Set `DEBUG = False`.
- Store `SECRET_KEY` securely in environment variables.
- Configure `ALLOWED_HOSTS` for the deployment environment.
- Use HTTPS and secure cookie settings.
- Configure a production-ready database.
- Review authentication, authorization, input validation, and error handling.
- Integrate a trusted payment gateway if real payments are required.

Never commit passwords, API keys, or other secrets to a public repository.

## Learning Outcomes

This project demonstrates practical experience with:

- Django application architecture and URL routing.
- Models, views, templates, and database migrations.
- User authentication and session management.
- CRUD operations through Django Admin.
- Shopping cart and order processing workflows.
- Responsive frontend development.
- Git and GitHub version control.

---

*NovaCart – An academic project demonstrating e-commerce application development using advanced web technologies.*