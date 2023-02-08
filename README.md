# venv Env activate

source venv/bin/activate
deactivate

## Update requirements.txt

pip freeze > requirements.txt
pip install -r requirements.txt

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

# Docker

docker build -t docker-flask:latest .
docker run --name microblog -d -p 8000:5000 --rm microblog:latest

# About translations

pybabel extract -F babel.cfg -k \_l -o messages.pot .

pybabel init -i messages.pot -d app/translations -l es
creating catalog app/translations/es/LC_MESSAGES/messages.po based on messages.pot

pybabel compile -d app/translations
compiling catalog app/translations/es/LC_MESSAGES/messages.po to
app/translations/es/LC_MESSAGES/messages.mo

## Update translations

pybabel extract -F babel.cfg -k \_l -o messages.pot .

pybabel update -i messages.pot -d app/translations

## Command-Line

flask translate init LANG to add a new language
flask translate update to update all language repositories
flask translate compile to compile all language repositories

# API

## Endpoints

| HTTP Method | Resource URL | Notes |
| --- | --- | --- |
| GET | /api/users/&lt;id&gt; | Return a user. |
| GET | /api/users | Return the collection of all users. |
| GET | /api/users/&lt;id&gt;/followers | Return the followers of this user. |
| GET | /api/users/&lt;id&gt;/followed | Return the users this user is following. |
| POST | /api/users | Register a new user account. |
| PUT | /api/users/&lt;id&gt; | Modify a user. |

### Token

- Return a token

$ http --auth <username>:<password> POST http://localhost:5000/api/tokens
- Return a user

$ http GET http://localhost:5000/api/users/1 "Authorization:Bearer pC1Nu9wwyNt8VCj1trWilFdFI276AcbS"


