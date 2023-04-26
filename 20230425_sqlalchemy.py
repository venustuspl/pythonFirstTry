
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost/demo'
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

def loadSomeData():
    p1 = Product('Bulbulator', 'Robi bul bul', 100)
    p2 = Product('Półoś do Jelcza', '3ma koło', 80)
    p3 = Product('Wahacz to taczki', 'Do taczek wyścigowych', 500)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()

def getOneProductById(productId):
    return Product.query.filter(Product.productId==productId).first()

def getAllProductsOrdered():
    return Product.query.order_by(Product.productPrice.desc()).all()

def getProductsPriceOver(p):
    return Product.query.filter(Product.productPrice > p).order_by(Product.productPrice).all()

def changePrice(product,newPrice):
    product.productPrice=newPrice
    db.session.add(product)
    db.session.commit()

def deleteProduct(product):
    db.session.delete(product)
    db.session.commit()

def showMeSQL(price):
    q=Product.query.filter(Product.productPrice>price)
    print(q)
    return q.all()

with app.app_context():
    #db.create_all()
    #loadSomeData()
    showMeSQL(1)