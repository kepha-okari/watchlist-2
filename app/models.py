from . import db #imports the database
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash# for pass hashing
from flask_login import UserMixin #LoginManager

# class User(UserMixin,db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     password_hash = db.Column(db.String(255))
#

class Movie:
    """Movie class to define Movie Objects"""

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count


class Review:
    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

class User(UserMixin,db.Model):#db.Model is assed as a parameter to conect to the database
    __tablename__ = 'users'#allows for proper naming of tables
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))#one to many relationship created
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    @login_manager.user_loader #model configuratiom
    def load_user(user_id):
        return User.query.get(int(user_id))
    # def __repr__(self):
    #     return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key =True)
    name =db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")#virtual column to connect with the foreign key
    pass_secure = db.Column(db.String(255))

    @property       # create write only property
    def password(self):
        raise AttributeError('You cannot read the pasword attribute')

    @password.setter
    def password(self):
        self.pass_secure = generate_password_hash(password)

    def password(self,password):
        return check_password_hash(self.pass_secure,password)
