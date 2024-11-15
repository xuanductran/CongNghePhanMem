from  sqlalchemy import Column, Integer, String,Float,ForeignKey,Boolean
from saleapp import app, db
from  sqlalchemy.orm import relationship


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(200), default="https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")
    active = Column(Boolean,default=True)


    def __str__(self):
        return self.name

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product',backref='category',lazy=True)
    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price=Column(Float,default=0)
    image=Column(String(200),default="https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")
    category_id= Column(Integer,ForeignKey(Category.id),nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Laptop")
        # c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()
        import json

        # with open('data/products.json', encoding='utf-8') as f:
        #     products = json.load(f)
        #     for p in products:
        #         prod=Product(**p)
        #         db.session.add(prod)
        # db.session.commit()
        import hashlib
        npass =str( hashlib.md5("123".encode("utf-8")).hexdigest())
        u=User(name="xuanduc",username="admin"
               ,password=npass)
        db.session.add(u)
        db.session.commit()