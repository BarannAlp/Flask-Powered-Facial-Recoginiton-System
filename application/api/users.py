from flask import Flask, jsonify, Blueprint,request
from application.models import User

apiUsers = Blueprint('apiUsers',__name__,url_prefix='/api/users')

@apiUsers.route('/')
def users():
    allUsers= User.get_all_users()
    users = []
    for user in allUsers:
        users.append({"id":user.id, "username": user.username,"password":user.password})
 
    return jsonify({"sucess":True, "data": users,"count":len(users)})

@apiUsers.route('/login',methods=["GET","POST"])
def loginUser():
  username=request.args.get("username")
  password=request.args.get("password")
  print(username,password)
  login = User.login_user(username,password)
  return jsonify({"sucess":login, "message": "authentication"})

