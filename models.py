from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect the database to the Flask app."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User table."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

class Post(db.Model):
    """Post table."""
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)  # Corrected column name
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    tags = db.relationship("Tag", secondary="post_tags", backref="posts_associated")
    #added for delete testing...cascade delete
    #tags = db.relationship("Tag", secondary="post_tags", backref="posts_associated", single_parent=True)
    #error: tags = db.relationship("Tag", secondary="post_tags", backref="posts_associated", cascade="all, delete-orphan")
class PostTag(db.Model):
    """Association table to link posts and tags."""
    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Tag(db.Model):
    """Tag table."""
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.Text, nullable=False, unique=True)
   
    db.relationship("Post", secondary="post_tags", backref="tags_associated")


   

#testing
#    @classmethod
#    def get_users_by_image_url(cls, image_url):
#        return cls.query.filter_by(image_url=image_url).all()

#not sure what to do with this:
#if __name__ == "__main__":
# So that we can use Flask-SQLAlchemy, we'll make a Flask app
#    from app import app
#    connect_db(app)
#removed below to not delete the database..
#
#    db.drop_all()
#    db.create_all()
   