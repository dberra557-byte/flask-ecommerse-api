from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# --- FLASK APP ---
app = Flask(__name__)

# --- DATABASE CONFIG ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Lovely123!@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- INIT DATABASE & MARSHMALLOW ---
db = SQLAlchemy(app)
ma = Marshmallow(app)

# --- DATABASE MODELS ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True)
    orders = db.relationship('Order', backref='user', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Float)
    orders = db.relationship('Order_Product', backref='product', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    products = db.relationship('Order_Product', backref='order', lazy=True)

class Order_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('order_id', 'product_id', name='_order_product_uc'),)

# --- MARSHMALLOW SCHEMAS ---
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True

class OrderProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order_Product
        include_fk = True

# --- TEST ROUTES ---
@app.route('/')
def home():
    return "Flask E-Commerce API is running!"

@app.route('/create_tables')
def create_tables():
    db.create_all()
    return "All tables created successfully!"

# --- RUN APP ---
if __name__ == '__main__':
    app.run(debug=True, port=5001)
