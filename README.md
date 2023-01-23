# venv Env activate

source venv/bin/activate

deactivate

# Flask shell usage

flask shell

# To use

    from app import app, db
    from app.models import User, Post

# Return users and posts

    User.query.get(1)
    Post.query.all()

# Create user

    user = User(username='Yasumitsu', email='yasumitsu@email.com')
    db.session.add(user)
    db.session.commit()

# Return posts from users

    user = User.query.get(1)
    posts = user.posts.all()

# Create a post

    user = User.query.get(1)
    post = Post(body='My post', author=user)
    db.session.add(post)
    db.session.commit()

# Querying user table

    users = User.query.all()
    for user in users:
        print(user.id, user.username)
