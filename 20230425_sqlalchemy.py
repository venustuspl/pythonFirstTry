
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://demo:demo@localhost/demo'
db=SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"
    productId = db.Column(db.Integer, name="product_id", primary_key=True)
    productName = db.Column(db.String, name="product_name", unique=True)
    productDescription = db.Column(db.String, name="product_description", nullable=True)
    productPrice = db.Column(db.Numeric, name="product_price", index=True)

    def __init__(self, pn, pd, pp):
        self.productName = pn
        self.productDescription = pd
        self.productPrice = pp

    def __str__(self):
        return f'productId={self.productId}, productName={self.productName}, productDescription={self.productDescription}, productPrice={self.productPrice}'

