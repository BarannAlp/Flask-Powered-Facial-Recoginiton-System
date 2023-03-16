from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
def createApp():
    app=Flask(__name__,instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/application'
    db.init_app(app)
   
    with app.app_context():
        
        db.create_all()
    return app