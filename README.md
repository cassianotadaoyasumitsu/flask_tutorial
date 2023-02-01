# venv Env activate

source venv/bin/activate
deactivate

## Update requirements.txt

pip freeze > requirements.txt

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

## Mysql Container

docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
 -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog \
 -e MYSQL_PASSWORD=<database-password> \
 mysql/mysql-server:latest

docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
 -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
 -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password> \
 --link mysql:dbserver \
 -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
 microblog:latest

## Elastic search Container

docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
 -e "discovery.type=single-node" \
 docker.elastic.co/elasticsearch/elasticsearch:8.6.1

docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
 -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
 -e MAIL_USERNAME=ctyasumitsu@gmail.com -e MAIL_PASSWORD=Cassian0 \
 --link mysql:dbserver \
 -e DATABASE_URL=mysql+pymysql://microblog:admin123@dbserver/microblog \
 --link elasticsearch:elasticsearch \
 -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
 microblog:latest
