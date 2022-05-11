from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import *

api=Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/dbcreateapi'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@api.route('/')
def hello():
    return '<h1> WELCOME IN OUR API</h1>'


@api.route('/groupe4/api/users', methods=["GET"])
def get_all_users():
    all_users=[]
    users = Users.query.all()
    for user in users:
        results = {
            "id":user.userid,
            "name":user.name,
            "username":user.username,
            "email":user.email,
            "Phone": user.phone,
            "Website":user.website,
        }
        all_users.append(results)
    return jsonify({
        "users":all_users
    })

db.init_app(api)
api.run(host='localhost', port=8000, debug=True)