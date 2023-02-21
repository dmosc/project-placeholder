import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import MySQLDatabase

load_dotenv()
app = Flask(__name__)
mysql_db = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
);

print(mysql_db)


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
