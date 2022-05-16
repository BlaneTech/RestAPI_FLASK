from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import *

api=Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/projetflask'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

URL='/groupe4/api/'

@api.route('/')
def hello():
    return '<h1> WELCOME IN OUR API</h1>'


@api.route(URL+'users', methods=["GET"])
def get_all_users():
    all_users=[]
    users = Users.query.all()
    address = Address.query.all()
    company = Company.query.all()
    for k in range(len(users)):
        user_results = {
            "id":users[k].userid,
            "name":users[k].name,
            "username":users[k].username,
            "email":users[k].email,
            "phone": users[k].phone,
            "website":users[k].website,
            "address":{
                "street":address[k].street,
                "suite":address[k].suite,
                "city":address[k].city,
                "zipcode":address[k].zipcode,
                "geo":{
                    "lat":address[k].geo_lat,
                    "lng":address[k].geo_lng
                },
            },
            "company":{
                "name":company[k].companyname,
                "catchPhrase":company[k].companycatchphrase,
                "bs":company[k].companybs
                },
        }
        all_users.append(user_results)
    # print(all_users)
    return jsonify(
        users=all_users
    )

@api.route(URL+'comments')
def get_all_comments():
    comments=Comment.query.all()
    all_comments=[]
    for comment in comments:
        comment_results={
            "postid":comment.postid,
            "name":comment.commentname,
            "email":comment.commentemail,
            "body":comment.commentbody,
        }
        all_comments.append(comment_results)
    return jsonify(Comments=all_comments)

@api.route(URL+'todos')
def get_all_todos():
    todos=Todo.query.all()
    all_todos=[]
    for todo in todos:
        todo_results={
            "userId":todo.userid,
            "id":todo.todoid,
            "title":todo.todotitle,
            "completed":todo.todoetat,
        }
        all_todos.append(todo_results)
    return jsonify(Todos=all_todos)

@api.route(URL+'albums')
def get_all_albums():
    albums=Albums.query.all()
    all_albums=[]
    for album in albums:
        album_results={
            "userId":album.userid,
            "id":album.albumid,
            "title":album.albumtitle
        }
        all_albums.append(album_results)
    return jsonify(All_albums=all_albums)

@api.route(URL+'photos')
def get_all_photos():
    photos=Photos.query.all()
    all_photos=[]
    for photo in photos:
        photo_results={
            "albumId":photo.albumid,
            "id":photo.photoid,
            "title":photo.phototitle,
            "url":photo.photourl,
            "thumbnailUrl":photo.photothumbnailurl,
        }
        all_photos.append(photo_results)
    return jsonify(all_photos=all_photos)

@api.route(URL+'users/<int:userid>')
def get_only_user(userid):
    user=Users.query.get(userid)
    address = Address.query.filter_by(userid=userid).first()
    company = Company.query.filter_by(userid=userid).first()
    one_user_result = {
            "id":user.userid,
            "name":user.name,
            "username":user.username,
            "email":user.email,
            "phone": user.phone,
            "website":user.website,
            "address":{
                "street":address.street,
                "suite":address.suite,
                "city":address.city,
                "zipcode":address.zipcode,
                "geo":{
                    "lat":address.geo_lat,
                    "lng":address.geo_lng
                },
            },
            "company":{
                "name":company.companyname,
                "catchPhrase":company.companycatchphrase,
                "bs":company.companybs
                },
        }
    return jsonify(user=one_user_result)

@api.route(URL+'users/<int:userid>/posts')
def get_posts_user(userid):
    all_posts_user=[]
    posts_users=Posts.query.filter_by(userid=userid).all()
    for  posts_user in posts_users:
        all_posts_user_result={
            "userid":posts_user.userid, 
            "id":posts_user.postid,
            "title":posts_user.posttitle,
            "body":posts_user.postbody  
        }
        all_posts_user.append(all_posts_user_result)
    return jsonify(posts_user=all_posts_user)

@api.route(URL+'users/<int:userid>/todos')
def get_todos_user(userid):
    all_todos_user=[]
    todos_users=Todo.query.filter_by(userid=userid).all()
    for  todo_user in todos_users:
        all_todos_user_result={
            "userid":todo_user.userid, 
            "id":todo_user.todoid,
            "title":todo_user.todotitle,
            "body":todo_user.todoetat  
        }
        all_todos_user.append(all_todos_user_result)
    return jsonify(todos_user=all_todos_user)


    




 
    


db.init_app(api)
api.run(host='localhost', port=8000, debug=True)