from dataclasses import dataclass
from application import db 
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

@dataclass
class Customer(db.Model):
    __tablename__='customer'

    id= db.Column(db.Integer,primary_key=True )
    date =db.Column(db.String(120))
    gender=db.Column(db.String(120))
    age= db.Column(db.Integer)

    def __init__(self,id,date,gender,age):
        self.id=id
        self.date=date
        self.gender=gender
        self.age=age

    @classmethod
    def get_all_customers(cls):
      return cls.query.all()
    
    @classmethod
    def add_customer(cls,id,date,gender,age):
        
        customer = cls(id=id,date=date,gender=gender,age=age)
        db.session.add(customer)
        db.session.commit()
        return 'added'
    
@dataclass
class User(db.Model):
    __tablename__='user'

   
    username =db.Column(db.String(120),primary_key=True)
    password=db.Column(db.String(120))
    

    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password

    @classmethod
    def get_all_users(cls):
        return cls.query.all()
    
    @classmethod
    def add_user(cls,username,password):
        user=cls(username,password)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete_user(cls,id):
        user=cls.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

    @classmethod
    def login_user(cls,username,password):
       
       user = cls.query.filter_by(username=username).first()
       if(user.password==password):
           login=True
       else:
            login = False
        
       return login