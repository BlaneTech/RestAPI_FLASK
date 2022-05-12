from crypt import methods
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import *

api=Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/projetflask'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@api.route('/')
def hello():
    return '<h1> WELCOME IN OUR API</h1>'


@api.route('/groupe4/api/users', methods=["GET"])
def get_all_users():
    all_users=[]
    users = Users.query.all()
    company = Company.query.all()
    for k in range(len(users)):
        user_results = {
            "id":users[k].userid,
            "name":users[k].name,
            "username":users[k].username,
            "email":users[k].email,
            "Phone": users[k].phone,
            "Website":users[k].website,
            
        }
        all_users.append(user_results)
    return jsonify({
        "users":all_users
    })

@api.route('/groupe4/api/posts', methods=["GET"])
def get_all_posts():
    all_posts = []
    posts = Posts.query.all()
    for post in posts:
        post_results = {
            "userId":post.userid,
            "id":post.postid,
            "title":post.posttitle,
            "body":post.postbody,
        }
        all_posts.append(post_results)
    return jsonify({"posts":all_posts})

@api.route('/groupe4/api/users/<int:userid>/albums')
def get_userid_albums(userid):
    albums_user = []
    albums = Albums.query.filter_by(userid=userid).all()
    for album in albums:
        all_users_albums = {
            "userid":album.userid,
            "id":album.albumid,
            "albumtitle":album.albumtitle,
        }

        albums_user.append(all_users_albums)
    return jsonify({
        "albums":albums_user
        })
     


db.init_app(api)
api.run(host='localhost', port=8000, debug=True)