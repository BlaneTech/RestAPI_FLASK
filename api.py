from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from database import *

api=Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/dbcreateapi'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api.config['JSON_SORT_KEYS']=False

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
    return jsonify(all_users)

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
    return jsonify(all_comments)

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
    return jsonify(all_todos)

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
    return jsonify(all_albums)

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
    return jsonify(all_photos)

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
    return jsonify(one_user_result)


@api.route(URL+'users/<int:userid>/photos')  
def get_all_photos_users(userid):
    all_photos_user=[]
    all_albums=Albums.query.filter_by(userid=userid).all()
    for album_user in all_albums:
        albumId = album_user.albumid
        all_photos=Photos.query.filter_by(albumid=albumId).all()
        for photos_user in all_photos:
            all_photos_user_results={
                "albumId":photos_user.albumid,
                "id":photos_user.photoid,
                "title":photos_user.phototitle,
                "url":photos_user.photourl,
                "thumbnailUrl":photos_user.photothumbnailurl,
            }
            all_photos_user.append(all_photos_user_results)
    return jsonify(all_photos_user)

@api.route(URL+'posts/<int:postid>/comments')
def get_all_comments_post(postid):
    all_comments_post=[]
    all_comment = Comment.query.filter_by(postid=postid).all()
    for comment_post in all_comment:
        all_comments_post_results={
            "postid":comment_post.postid,
            "id":comment_post.commentid,
            "name":comment_post.commentname,
            "email":comment_post.commentemail,
            "body":comment_post.commentbody,
        }
        all_comments_post.append(all_comments_post_results)
    return jsonify(all_comments_post)

@api.route(URL+'albums/<int:albumid>/photos')
def get_all_photos_album(albumid):
    all_photos_album = []
    all_photos = Photos.query.filter_by(albumid=albumid).all()
    for photos_album in all_photos:
        photos_album_results={
            "albumId":photos_album.albumid,
            "id":photos_album.photoid,
            "title":photos_album.phototitle,
            "url":photos_album.photourl,
            "thumbnailUrl":photos_album.photothumbnailurl,
        }
        all_photos_album.append(photos_album_results)
    return jsonify(all_photos_album)


@api.route(URL+'posts', methods=["GET"])
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
    return jsonify(all_posts)

@api.route(URL+'users/<int:userid>/albums')
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
    return jsonify(albums_user)
    
# POST REQUEST
def gestionId(table_name, col_name):
    list_id=set()
    ids = table_name.query.with_entities(col_name).all()
    for id in ids:
        list_id.add(id[0])
    return max(list_id)+1

@api.route(URL+'user', methods=['POST'])
def add_user():
    # data foer table Users
    name=request.json['name']
    username=request.json['username']
    email=request.json['email']
    phone= request.json['phone'],
    website=request.json['website']
    
    # data for table Address
    street=request.json['street']
    suite=request.json['suite']
    city=request.json['city']
    zipcode = request.json['zipcode']
    lat = request.json['lat']
    lng = request.json['lng']

    #data for table Company 
    company_name = request.json['company_name']
    catchPhrase = request.json['catchPhrase']
    bs = request.json['bs']    

    userid=gestionId(Users,Users.userid)
    addressid=gestionId(Address,Address.addressid)
    companyid=gestionId(Company,Company.companyid)
    new_user = Users(userid=userid, name=name, username=username,email=email, phone=phone, website=website)

    new_address = Address(addressid=addressid, street=street, suite=suite, city=city, zipcode=zipcode, geo_lat = lat, geo_lng=lng,userid=userid)
    
    new_company = Company(companyid=companyid, companyname=company_name, companycatchphrase=catchPhrase, companybs=bs,userid=userid)
    if Users.query.filter_by(email=email).count() == 0:
        db.session.add(new_user)
        db.session.add(new_address)
        db.session.add(new_company)
        db.session.commit()
        return "ok"
    else:
        return "Email already exist"


@api.route(URL+'users/<int:userid>/albums',methods=['POST'])
def add_album(userid):
    userid=request.json['userid']
    # print(request,userid)
    albumtitle=request.json['albumtitle']
    albumid=gestionId(Albums,Albums.albumid)
    new_album=Albums(albumid=albumid, userid=userid,albumtitle=albumtitle)
    db.session.add(new_album)
    db.session.commit()
    #print(userid,albumtitle,"sidhfifhif")
    return "ok"

db.init_app(api)
api.run(host='localhost', port=8000, debug=True)

