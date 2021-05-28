from datetime import datetime, timezone
from enum import unique

from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    full_name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    image_file = db.Column(db.String(20),default='default.jpg')
    # upload = db.relationship('Upload')
    # order_list = db.relationship('Order_List')
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}' )"

# class Upload():
#     id = db.Column(db.Integer, primary_key=True)
#     # user_email = db.Column(db.String(150), db.ForeignKey('user.id'))



# class Product():
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     price = db.Column(db.Integer, nullable= False)
#     description = db.Column(db.String(150), unique=True)
#     available = db.Column(db.Boolean, nullable=False)
#     categories = db.Column(db.String(150), unique=True, nullable=False)
#     item = db.Column(db.String(150))
#     code = db.Column(db.String(150))
#     item_picture = db.Column(db.String(150), unique=True, default = 'itemdefault.jpg')


# class Admin():
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy = True)


# class Order_List():
#     id = db.Column(db.Integer, primary_key=True)
#     # order_data = db.Column(db.Datatime(timezone=True), default=func.now(), unique=True)
#     # delivary_data = db.Column(db.Datatime(timezone=True), default=func.now(), unique=True)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     address_user = db.Column(db.String(150), nullable=False)
