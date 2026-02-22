E-Commerce API with Flask & MySQL
Overview
This project is a fully functional RESTful e-commerce API built with Flask, Flask-SQLAlchemy, Flask-Marshmallow, and MySQL. It manages Users, Orders, and Products, including proper relationships:
One-to-Many: One User → Many Orders
Many-to-Many: Orders ↔ Products (via association table)
The API supports CRUD operations, serialization, and input validation using Marshmallow.
Features
User Management: Create, read, update, delete users.
Product Management: Create, read, update, delete products.
Order Management:
Create orders for users
Add/remove products from orders (prevents duplicates)
List all orders for a user
List all products in an order
Technologies Used
Python 3.x
Flask
Flask-SQLAlchemy
Flask-Marshmallow
MySQL
Marshmallow-SQLAlchemy
Installation
Clone the repo
Bash
Copy code
git clone <your-repo-url>
cd <your-repo-folder>
Set up virtual environment
Bash
Copy code
python3 -m venv venv
source venv/bin/activate # Mac/Linux
# or
venv\Scripts\activate # Windows
Install dependencies
Bash
Copy code
pip install Flask Flask-SQLAlchemy Flask-Marshmallow marshmallow-sqlalchemy mysql-connector-python
Set up MySQL database
SQL
Copy code
CREATE DATABASE ecommerce_api;
Update your app.py database URI:
Python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:<YOUR_PASSWORD>@localhost/ecommerce_api'
Run the app
Bash
Copy code
python app.py
The API will run on http://127.0.0.1:5000/
API Endpoints
Users
GET /users — Get all users
GET /users/<id> — Get user by ID
POST /users — Create a new user
PUT /users/<id> — Update user
DELETE /users/<id> — Delete user
Products
GET /products — Get all products
GET /products/<id> — Get product by ID
POST /products — Create product
PUT /products/<id> — Update product
DELETE /products/<id> — Delete product
Orders
POST /orders — Create order (requires user_id and optional order_date)
PUT /orders/<order_id>/add_product/<product_id> — Add product to order
DELETE /orders/<order_id>/remove_product/<product_id> — Remove product from order
GET /orders/user/<user_id> — Get all orders for a user
GET /orders/<order_id>/products — Get all products in an order
Testing
Use Postman or cURL to test endpoints.
Verify data storage in MySQL Workbench.
Ensure the association table prevents duplicate products in an order.
