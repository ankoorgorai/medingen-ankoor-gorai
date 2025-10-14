from database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    salt_content = db.Column(db.Float)
    price = db.Column(db.Float)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    reviewer = db.Column(db.String(100))
    comment = db.Column(db.String(255))
