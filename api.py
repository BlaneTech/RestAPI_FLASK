from flask import Flask, flash, jsonify, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_jsglue import JSGlue
from database import *

api = Flask(__name__)
# jsglue = JSGlue(api)

CORS(api)
api.config['SECRET_KEY'] = 'groupe4'
api.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:test123@localhost/projetflask"
api.config['CORS_HEADERS'] = 'Content-Type'
api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
api.config["JSON_SORT_KEYS"] = False

URL = "/groupe4/api/"

@api.route('/')
def login():
    return render_template('pageLogin.html')


@api.route("/display_user")
def display_user():
    return render_template('affiche_user.html')


@api.route('/new_user')
def new_user():
    return render_template('add_user.html')


@api.route('/user_page')
def user_page():
    return render_template('user.html')


@api.route('/sign_in', methods=['POST'])
def sign_in():
    utilisateurs = Utilisateurs.query.all()
    temp=0
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        for utilisateur in utilisateurs:
            if utilisateur.username == username and utilisateur.password == password:
                profil = utilisateur.profil
                return redirect('display_user')
            else:
                temp+=1
        if temp == 3:
            flash("Usename or password invalide")
            return redirect('/')
        

@api.route('/add_user')
def add_user_page():
    return redirect('add_user.html')


@api.route(URL + "users", methods=["GET"])
def get_all_users():
    all_users = []
    users = Users.query.filter_by(archive=1).order_by(Users.userid.desc()).all()
    address = Address.query.filter_by(archive=1).order_by(Address.addressid.desc()).all()
    company = Company.query.filter_by(archive=1).order_by(Company.companyid.desc()).all()
    for k in range(len(users)):
        user_results = {
            "id": users[k].userid,
            "name": users[k].name,
            "username": users[k].username,
            "email": users[k].email,
            "phone": users[k].phone,
            "website": users[k].website,
            "address": {
                "street": address[k].street,
                "suite": address[k].suite,
                "city": address[k].city,
                "zipcode": address[k].zipcode,
                "geo": {"lat": address[k].geo_lat, "lng": address[k].geo_lng},
            },
            "company": {
                "name": company[k].companyname,
                "catchPhrase": company[k].companycatchphrase,
                "bs": company[k].companybs,
            },
        }
        all_users.append(user_results)
    # print(all_users)
    return jsonify(all_users)


@api.route(URL + "comments")
def get_all_comments():
    comments = Comment.query.filter_by(archive=1).all()
    all_comments = []
    for comment in comments:
        comment_results = {
            "postid": comment.postid,
            "name": comment.commentname,
            "email": comment.commentemail,
            "body": comment.commentbody,
        }
        all_comments.append(comment_results)
    return jsonify(all_comments)


@api.route(URL + "todos")
def get_all_todos():
    todos = Todo.query.filter_by(archive=1).all()
    all_todos = []
    for todo in todos:
        todo_results = {
            "userId": todo.userid,
            "id": todo.todoid,
            "title": todo.todotitle,
            "completed": todo.todoetat,
        }
        all_todos.append(todo_results)
    return jsonify(all_todos)


@api.route(URL + "albums")
def get_all_albums():
    albums = Albums.query.filter_by(archive=1).all()
    all_albums = []
    for album in albums:
        album_results = {
            "userId": album.userid,
            "id": album.albumid,
            "title": album.albumtitle,
        }
        all_albums.append(album_results)
    return jsonify(all_albums)


@api.route(URL + "photos")
def get_all_photos():
    photos = Photos.query.filter_by(archive=1).all()
    all_photos = []
    for photo in photos:
        photo_results = {
            "albumId": photo.albumid,
            "id": photo.photoid,
            "title": photo.phototitle,
            "url": photo.photourl,
            "thumbnailUrl": photo.photothumbnailurl,
        }
        all_photos.append(photo_results)
    return jsonify(all_photos)


@api.route(URL + "users/<int:userid>")
def get_only_user(userid):
    user = Users.query.get(userid)
    address = Address.query.filter_by(userid=userid, archive=1).first()
    company = Company.query.filter_by(userid=userid, archive=1).first()
    one_user_result = {
        "id": user.userid,
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "phone": user.phone,
        "website": user.website,
        "address": {
            "street": address.street,
            "suite": address.suite,
            "city": address.city,
            "zipcode": address.zipcode,
            "geo": {"lat": address.geo_lat, "lng": address.geo_lng},
        },
        "company": {
            "name": company.companyname,
            "catchPhrase": company.companycatchphrase,
            "bs": company.companybs,
        },
    }
    return jsonify(one_user_result)


@api.route(URL + "users/<int:userid>/photos")
def get_all_photos_users(userid):
    all_photos_user = []
    all_albums = Albums.query.filter_by(userid=userid, archive=1).all()
    for album_user in all_albums:
        albumId = album_user.albumid
        all_photos = Photos.query.filter_by(albumid=albumId, archive=1).all()
        for photos_user in all_photos:
            all_photos_user_results = {
                "albumId": photos_user.albumid,
                "id": photos_user.photoid,
                "title": photos_user.phototitle,
                "url": photos_user.photourl,
                "thumbnailUrl": photos_user.photothumbnailurl,
            }
            all_photos_user.append(all_photos_user_results)
    return jsonify(all_photos_user)


@api.route(URL + "posts/<int:postid>/comments")
def get_all_comments_post(postid):
    all_comments_post = []
    all_comment = Comment.query.filter_by(postid=postid, archive=1).all()
    for comment_post in all_comment:
        all_comments_post_results = {
            "postid": comment_post.postid,
            "id": comment_post.commentid,
            "name": comment_post.commentname,
            "email": comment_post.commentemail,
            "body": comment_post.commentbody,
        }
        all_comments_post.append(all_comments_post_results)
    return jsonify(all_comments_post)


@api.route(URL + "albums/<int:albumid>/photos")
def get_all_photos_album(albumid):
    all_photos_album = []
    all_photos = Photos.query.filter_by(albumid=albumid, archive=1).all()
    for photos_album in all_photos:
        photos_album_results = {
            "albumId": photos_album.albumid,
            "id": photos_album.photoid,
            "title": photos_album.phototitle,
            "url": photos_album.photourl,
            "thumbnailUrl": photos_album.photothumbnailurl,
        }
        all_photos_album.append(photos_album_results)
    return jsonify(all_photos_album)


@api.route(URL + "users/<int:userid>/todos")
def get_all_user_todos(userid):
    all_todos_user = []
    all_todos = Todo.query.filter_by(userid=userid, archive=1).all()
    for tod in all_todos:
        all_todo_results = {
            "id": tod.todoid,
            "todotitle": tod.todotitle,
            "todoetat": tod.todoetat,
        }
        all_todos_user.append(all_todo_results)
    return jsonify(all_todos_user)


@api.route(URL + "comment/<int:commentid>")
def get_all_comment(commentid):
    all_commentid = []
    all_comment = Comment.query.filter_by(commentid=commentid, archive=1).all()
    for comment_id in all_comment:
        all_commentid_results = {
            "postid": comment_id.postid,
            "name": comment_id.commentname,
            "email": comment_id.commentemail,
            "body": comment_id.commentbody,
        }
        all_commentid.append(all_commentid_results)
    return jsonify(all_commentid)


@api.route(URL + "posts/<int:postid>")
def get_all_postid(postid):
    all_postid = []
    all_posts = Posts.query.filter_by(postid=postid, archive=1)
    for post_id in all_posts:
        all_postid_results = {
            "posttitle": post_id.posttitle,
            "body": post_id.postbody,
            "userid": post_id.userid,
        }
        all_postid.append(all_postid_results)
    return jsonify(all_postid)


@api.route(URL + "posts", methods=["GET"])
def get_all_posts():
    all_posts = []
    posts = Posts.query.filter_by(archive=1).all()
    for post in posts:
        post_results = {
            "userId": post.userid,
            "id": post.postid,
            "title": post.posttitle,
            "body": post.postbody,
        }
        all_posts.append(post_results)
    return jsonify(all_posts)


@api.route(URL + "users/<int:userid>/albums")
def get_userid_albums(userid):
    albums_user = []
    albums = Albums.query.filter_by(userid=userid, archive=1).all()
    for album in albums:
        all_users_albums = {
            "userid": album.userid,
            "id": album.albumid,
            "albumtitle": album.albumtitle,
        }
        albums_user.append(all_users_albums)
    return jsonify(albums_user)


########################################
########## POST REQUEST #################
###############################"#########


def gestion_id(table_name, col_name):
    list_id = set()
    ids = table_name.query.with_entities(col_name).all()
    for id in ids:
        list_id.add(id[0])
    return max(list_id) + 1


@api.route(URL + "user", methods=["POST"])
def add_user():
    # data foer table Users
    name = request.json["name"]
    username = request.json["username"]
    email = request.json["email"]
    phone = (request.json["phone"],)
    website = request.json["website"]

    # data for table Address
    street = request.json["street"]
    suite = request.json["suite"]
    city = request.json["city"]
    zipcode = request.json["zipcode"]
    lat = request.json["lat"]
    lng = request.json["lng"]

    # data for table Company
    company_name = request.json["company_name"]
    catchPhrase = request.json["catchPhrase"]
    bs = request.json["bs"]

    userid = gestion_id(Users, Users.userid)
    addressid = gestion_id(Address, Address.addressid)
    companyid = gestion_id(Company, Company.companyid)
    new_user = Users(
        userid=userid,
        name=name,
        username=username,
        email=email,
        phone=phone,
        website=website,
    )

    new_address = Address(
        addressid=addressid,
        street=street,
        suite=suite,
        city=city,
        zipcode=zipcode,
        geo_lat=lat,
        geo_lng=lng,
        userid=userid,
    )

    new_company = Company(
        companyid=companyid,
        companyname=company_name,
        companycatchphrase=catchPhrase,
        companybs=bs,
        userid=userid,
    )
    if Users.query.filter_by(email=email).count() == 0:
        db.session.add(new_user)
        db.session.add(new_address)
        db.session.add(new_company)
        db.session.commit()
        return "ok"
    else:
        return "Email already exist"


@api.route(URL + "users/<int:userid>/albums", methods=["POST"])
def add_album(userid):
    userid = request.json["userid"]
    albumtitle = request.json["albumtitle"]
    albumid = gestion_id(Albums, Albums.albumid)
    new_album = Albums(albumid=albumid, userid=userid, albumtitle=albumtitle)
    db.session.add(new_album)
    db.session.commit()
    return "ok"


@api.route(URL + "users/<int:userid>/todo", methods=["POST"])
def add_todo(userid):
    # userid = request.json["userid"]
    todotitle = request.json["todotitle"]
    todoetat = request.json["todoetat"]
    todoid = gestion_id(Todo, Todo.todoid)
    new_todo = Todo(
        todoid=todoid, userid=userid, todotitle=todotitle, todoetat=todoetat
    )
    db.session.add(new_todo)
    db.session.commit()
    return "Todo ajouter"


@api.route(URL + "users/<int:userid>/posts", methods=["POST"])
def add_post(userid):
    posttitle = request.json["posttitle"]
    postbody = request.json["postbody"]
    postid = gestion_id(Posts, Posts.postid)
    new_post = Posts(
        postid=postid, userid=userid, posttitle=posttitle, postbody=postbody
    )
    db.session.add(new_post)
    db.session.commit()
    return "Post ajouter"


@api.route(URL + "albums/<int:albumid>/photos", methods=["POST"])
def add_photo(albumid):
    # albumid = request.json["albumid"]
    phototitle = request.json["phototitle"]
    photourl = request.json["photourl"]
    photothumbnailurl = request.json["photothumbnailurl"]
    photoid = gestion_id(Photos, Photos.photoid)
    new_photo = Photos(
        photoid=photoid,
        albumid=albumid,
        phototitle=phototitle,
        photourl=photourl,
        photothumbnailurl=photothumbnailurl,
    )
    db.session.add(new_photo)
    db.session.commit()
    return "Photo ajouter"


###################################################
################# PATCH REQUEST####################
@api.route(URL+'users/<int:userid>', methods=["PATCH"])
def update_user(userid):
    user = Users.query.filter_by(userid=userid, archive=1).first()
    user_address = Address.query.filter_by(userid=userid, archive=1).first()
    user_company = Company.query.filter_by(userid=userid, archive=1).first()
    
    user.name = request.json['name'] if 'name' in request.json else user.name
    user.username = request.json['username'] if 'username' in request.json else user.username
    user.email =  request.json['email'] if 'email' in request.json else user.email
    user.phone = request.json['website'] if 'phone' in request.json else user.phone
    user.website = request.json['website'] if 'website' in request.json else user.website
    
    user_address.street = request.json['street'] if 'street' in request.json else user_address.street
    user_address.suite = request.json['suite'] if 'suite' in request.json else user_address.suite
    user_address.city = request.json['city'] if 'city' in request.json else user_address.city
    user_address.zipcode =request.json['zipcode'] if 'zipcode' in request.json else user_address.zipcode
    user_address.geo_lat = request.json['lat'] if 'lat' in request.json else user_address.geo_lat
    user_address.geo_lng = request.json['lng'] if 'lng' in request.json else user_address.geo_lng

    user_company.companyname = request.json['company_name'] if 'company_name' in request.json else user_company.companyname
    user_company.companycatchphrase = request.json['catchphrase'] if 'catchphrase' in request.json else user_company.companycatchphrase
    user_company.companybs = request.json['bs'] if 'bs' in request.json else user_company.companybs
    
    db.session.commit()
    
    return jsonify({"update user": "success"})

@api.route(URL + "todos/<int:todoid>", methods=["PATCH"])
def update_todo(todoid):
    todo = Todo.query.filter_by(todoid=todoid, archive=1).first()
    todo.todoetat = request.json["completed"]
    todo.todotitle = request.json["title"]
    db.session.commit()
    return "todo modifier"


@api.route(URL + "photos/<int:photoid>", methods=["PATCH"])
def update_photo(photoid):
    photo = Photos.query.filter_by(photoid=photoid, archive=1).first()
    photo.phototitle = request.json["title"]
    photo.photourl = request.json["url"]
    photo.photothumbnailurl = request.json["thumbnailUrl"]
    db.session.commit()
    return "photo modifier"


@api.route(URL + "comments/<int:commentid>", methods=["PATCH"])
def update_comment(commentid):
    comment = Comment.query.filter_by(commentid=commentid, archive=1).first()
    comment.commentname = request.json["name"]
    comment.commentemail = request.json["email"]
    comment.commentbody = request.json["body"]
    db.session.commit()
    return "commentaire modifier"


@api.route(URL + "albums/<int:albumid>", methods=["PATCH"])
def update_albums(albumid):
    update_album = Albums.query.filter_by(albumid=albumid, archive=1).first()
    albumtitle = request.json["albumtitle"]
    update_album.albumtitle = albumtitle
    db.session.commit()
    return "ok"


@api.route(URL + "posts/<int:postid>", methods=["PATCH"])
def update_post(postid):
    post = Posts.query.filter_by(postid=postid, archive=1).first()
    post.posttitle = request.json["title"]
    post.postbody = request.json["body"]
    db.session.commit()
    return "post modifier"


##############################################
###################DELETE REQUEST #############
###############################################
status = 0


@api.route(URL + "albums/<int:albumid>", methods=["DELETE"])
def archive_one_album(albumid):
    archive_album = Albums.query.filter_by(albumid=albumid, archive=1).first()
    archive_photos_album = Photos.query.filter_by(albumid=albumid, archive=1).all()

    for photo in archive_photos_album:
        photo.archive = status
    archive_album.archive = status
    db.session.commit()
    return "succesfull"


@api.route(URL + "todos/<int:todoid>", methods=["DELETE"])
def archive_one_todo(todoid):
    archive_todo = Todo.query.filter_by(todoid=todoid, archive=1).first()
    archive_todo.archive = status
    db.session.commit()
    return "Suppression valider"


@api.route(URL + "comments/<int:commentid>", methods=["DELETE"])
def archive_one_comment(commentid):
    archive_comment = Comment.query.filter_by(commentid=commentid, archive=1).first()
    archive_comment.archive = status
    db.session.commit()
    return "commentaire supprimer"


@api.route(URL + "posts/<int:postid>", methods=["DELETE"])
def archive_one_post(postid):
    archive_post = Posts.query.filter_by(postid=postid, archive=1).first()
    archive_post.archive = status
    db.session.commit()
    return "post supprimer"


@api.route(URL + "photos", methods=["DELETE"])
def archive_all_photos():
    all_photo = Photos.query.filter_by(archive=1).all()
    status = request.json["status"]
    for photo in all_photo:
        photo.archive = status
    db.session.commit()
    return "ALL post are delete"


@api.route(URL + "posts", methods=["DELETE"])
def archive_all_posts():
    all_posts = Posts.query.filter_by(archive=1).all()
    all_comment = Comment.query.filter_by(archive=1).all()
    for comment in all_comment:
        comment.archive = status
    for post in all_posts:
        post.archive = status
    db.session.commit()
    return "Suppression effectuer"


@api.route(URL + "users/<int:userid>/albums", methods=["DELETE"])
def archive_all_albums_user(userid):
    one_user = Users.query.filter_by(userid=userid, archive=1).first()
    all__albums = Albums.query.filter_by(userid=one_user.userid, archive=1).all()
    for albums in all__albums:
        all_photos = Photos.query.filter_by(albumid=albums.albumid, archive=1).all()
        for photo in all_photos:
            photo.archive = status
        albums.archive = status
    db.session.commit()
    return "valider"


@api.route(URL + "users/<int:userid>/todos", methods=["DELETE"])
def archive_all_todos_user(userid):
    one_user = Users.query.filter_by(userid=userid, archive=1).first()
    all__todos = Todo.query.filter_by(userid=one_user.userid, archive=1).all()
    for todo in all__todos:
        todo.archive = status
    db.session.commit()
    return "valider"


@api.route(URL + "todos", methods=["DELETE"])
def archive_all_todos():
    all_todos = Todo.query.fiter_by(archive=1).all()
    for todo in all_todos:
        todo.archive = status
    db.session.commit()
    return "archive all todos succesfully"


@api.route(URL + "albums/<int:albumid>/photos", methods=["DELETE"])
def archive_all_photos_in_a_album(albumid):
    all_photos = Photos.query.filter_by(albumid=albumid, archive=1)
    for photo in all_photos:
        photo.archive = status
    db.session.commit()
    return "all photos are succesfully archived"


@api.route(URL + "albums", methods=["DELETE"])
def archive_all_albums():
    all_albums = Albums.query.filter_by(archive=1).all()
    for album in all_albums:
        album.archive = status
    db.session.commit()
    return "tous les albums sont archiv??s"


@api.route(URL + "photos/<int:photoid>", methods=["DELETE"])
def archive_one_photo(photoid):
    archive_photo = Photos.query.filter_by(photoid=photoid, archive=1).first()
    archive_photo.archive = status
    db.session.commit()
    return "photo archiv??e"


@api.route(URL + "users/<int:userid>/posts", methods=["DELETE"])
def archive_all_post_user(userid):
    archive_all_post = Posts.query.filter_by(userid=userid, archive=1).all()
    archive_all_post.archive = status
    db.session.commit()
    return "all posts are succesfully archived"


@api.route(URL+'users/<int:userid>', methods=['DELETE'])
def archive_a_user(userid):
    user = Users.query.filter_by(userid=userid, archive=1).first()
    user.archive = status
    user_address = Address.query.filter_by(userid=userid, archive=1).first()
    user_address.archive = status
    user_company = Company.query.filter_by(userid=userid, archive=1).first()
    user_company.archive = status
    all_user_posts= Posts.query.filter_by(userid=userid, archive=1).all()
    for post in all_user_posts:
        post.archive = status
        all_user_comment = Comment.query.filter_by(postid=post.postid, archive=1).all()
        for comment in all_user_comment:
            comment.archive = status
    all_user_todos = Todo.query.filter_by(userid=userid, archive=1).all()
    for todo in all_user_todos:
        todo.archive = status
    all_user_albums = Albums.query.filter_by(userid=userid).all()
    for album in all_user_albums:
        album.archive = status
        all_user_photos = Photos.query.filter_by(albumid = album.albumid, archive=1).all()
        for photo in all_user_photos:
            photo.archive = status
    
    db.session.commit()
    return jsonify({"delete_user": "success"})        


db.init_app(api)
api.run(host="localhost", port=8000, debug=True)
