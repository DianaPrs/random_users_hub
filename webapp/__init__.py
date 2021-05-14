from flask import Flask, render_template, request, redirect, flash
from flask_pymongo import PyMongo
from webapp.forms import UserForm
from webapp.upload_user import get_user

def create_app():
    """Application factory"""
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    mongo = PyMongo(app)
    db = mongo.db

    @app.route("/")
    def main_page():
        """"""
        users = db.users.find()
        if not users.count():
            db.users.insert_many(get_user(1000))
        return render_template("index.html", users=users)

    @app.route("/upload", methods=['POST'])
    def upload():
        """"""
        num = request.form['number']
        user = get_user(num)
        if user:
            db.users.insert_many(user)
            flash("Successfully added")
        else:
            flash("Data upload failed")
        return redirect(request.referrer)

    @app.route("/user/<username>")
    def user_profile(id):
        user = db.users.find_one_or_404({"_id": id})
        return render_template("user.html", user=user)

    @app.route("/user/new")
    def new_user():
        user_form = UserForm()
        return render_template("new_user.html", form=user_form)

    @app.route("/delete_todo/<int:todoId>", methods=['DELETE'])
    def delete_user(id):
        todo = db.user.delete_one({'_id': id})
        return ""

    @app.route("/update_user/<int:id>")
    def update_user(id):
        result = db.users.update_one({'_id': id}, {"name": {"first": "Nono"}})
        return ""

    #db.colection.insert_many() method. The insert_many() method take a list of dictionaries
    # db.users.insert_one()

    return app