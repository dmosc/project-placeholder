import os
import json

from flask import Flask, render_template, request, redirect
from peewee import MySQLDatabase
from playhouse.shortcuts import model_to_dict

from app.database.lib import Database
from app.database.models.post import Post


app = Flask(__name__)
database = Database.get_instance()

database.connect()
database.create_tables([Post])
print(database.get_tables())

@app.route('/')
def index():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('index.html', title="Week 1 - Team Portfolio", url=os.getenv("URL"), users=data["users"])


@app.route('/map')
def map_view():
    return render_template('map.html')


@app.route('/aboutme')
def aboutme():
    with open("app/data.json") as file:
        data = json.load(file)
        return render_template('aboutme.html', title="Week 1 - Team Portfolio", url=os.getenv("URL"), users=data["users"])


@app.route("/<path:path>")
def catch_all(path):
    return render_template("404.html", path=path)


@app.route("/api/create_post", methods=["POST"])
def create_post():
    payload = request.get_json()
    name = payload['name']
    email = payload['email']
    content = payload['content']
    post = Post.create(name=name, email=email, content=content)

    return model_to_dict(post)


@app.route("/api/get_posts", methods=["GET"])
def get_posts():
    found_posts = Post.select().order_by(Post.created_at.desc())
    posts = [model_to_dict(p) for p in found_posts]

    return { "posts": posts }


@app.route("/api/delete_posts", methods=["DELETE"])
def delete_posts():
    Post.delete().execute()
    return redirect("/api/get_posts")
