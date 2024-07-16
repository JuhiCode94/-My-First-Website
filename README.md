# Juhi Sweets Website

This is a Django-based website for Juhi Sweets, showcasing various products like cakes, chocolates, and ice creams. The website allows users to browse products, place orders, subscribe to newsletters, and contact the shop.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- Browse products: Cakes, Chocolates, and Ice Creams.
- Place orders and view order summaries.
- Subscribe to newsletters.
- Contact form to send messages to the shop.
- Search functionality to find specific products.
- Admin panel to manage products, orders, and subscribers.

## Setup

**Create a virtual environment and activate it:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

**Install the required packages:**

    ```
    pip install -r requirements.txt
    ```

**Apply migrations:**

    ```
    python manage.py migrate
    ```

### Prerequisites

- Python 3.11.4 or higher
- Django 5.0.6

**Apply migrations:**

    ```sh
    python manage.py migrate
    ```

**Run the development server:**

    ```sh
    python manage.py runserver
    ```

**Open your browser and navigate to:** `http://127.0.0.1:8000`

### Usage

#### URLs and Views

- **Home Page:** `http://127.0.0.1:8000/`
- **About Page:** `http://127.0.0.1:8000/about`
- **Cake Page:** `http://127.0.0.1:8000/cake`
- **Chocolate Page:** `http://127.0.0.1:8000/chocolate`
- **Ice Cream Page:** `http://127.0.0.1:8000/icecream`
- **Privacy Policy Page:** `http://127.0.0.1:8000/privacy`
- **Terms and Conditions Page:** `http://127.0.0.1:8000/terms`
- **Contact Page:** `http://127.0.0.1:8000/contact`
- **Order Confirmation Page:** `http://127.0.0.1:8000/order_confirmation`
- **Order Summary Page:** `http://127.0.0.1:8000/order_summary`
- **Subscription Page:** `http://127.0.0.1:8000/subscribe`
- **Search Results Page:** `http://127.0.0.1:8000/search_results`

#### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin` with the following credentials:

- **Username:** admin
- **Password:** admin_password

### Project Structure

```plaintext
juhi-sweets/
├── home/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── cake.html
│   │   ├── chocolate.html
│   │   ├── icecream.html
│   │   ├── privacy.html
│   │   ├── terms.html
│   │   ├── contact.html
│   │   ├── order_confirmation.html
│   │   ├── order_summary.html
│   │   └── search_results.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
