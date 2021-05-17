from flask import Flask, render_template, request, redirect, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from webapp.forms import UserForm
from webapp.upload_user import get_user
import random


def create_app():
    """Application factory"""
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    mongo = PyMongo(app)
    db = mongo.db

    @app.route("/")
    def index():
        """Main page route"""
        users = db.users.find()
        # if not users.count():
        #     db.users.insert_many(get_user(1000))
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
        return redirect(url_for("index"))

    @app.route("/user/<user_id>")
    def user_profile(user_id):
        """"""
        user = db.users.find_one_or_404({"_id": ObjectId(user_id)})
        return render_template("user.html", user=user)

    @app.route("/user/new", methods=['POST', 'GET'])
    def new_user():
        """"""
        form = UserForm()
        if form.validate_on_submit():
            data = {"name": {"first": form.first_name.data, "last": form.last_name.data},
                    "gender": form.gender.data, "cell": form.phone.data,
                    "email": form.email.data, "location": {
                    "city": form.city.data, "country": form.country.data,
                    "street": {"name": form.street.data}},
                    "picture": {"large": form.picture.data}
                    }
            db.users.insert_one(data)
            flash("Successfully added")
            user = db.users.find_one_or_404({"email": form.email.data})
            return render_template("user.html", user=user)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash("Mistake in field '{}': - {}".format(
                        getattr(form, field).label.text, error
                    ))
        return render_template("new_user.html", form=form)

    @app.route("/update_user/<user_id>", methods=['POST', 'GET'])
    def update_user(user_id):
        """"""
        form = UserForm()
        if form.validate_on_submit():
            data = {"name": {"first": form.first_name.data, "last": form.last_name.data},
                    "gender": form.gender.data, "cell": form.phone.data,
                    "email": form.email.data, "location": {
                    "city": form.city.data, "country": form.country.data,
                    "street": {"name": form.street.data}},
                    "picture": {"large": form.picture.data}
                    }
            db.users.find_one_and_replace({'_id': ObjectId(user_id)}, data)
            flash("Successfully added")
            user = db.users.find_one_or_404({"_id": ObjectId(user_id)})
            return render_template("user.html", user=user)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash("Mistake in field '{}': - {}".format(
                        getattr(form, field).label.text, error
                    ))
        user = db.users.find_one_or_404({"_id": ObjectId(user_id)})
        return render_template("update_user.html", user=user, form=form)

    @app.route("/random")
    def random_user():
        """"""
        users = db.users.find()
        if users:
            user = random.choice([user for user in users])
            return render_template("user.html", user=user)
        flash("Failed to get random user")
        return redirect(url_for("index"))

    @app.route("/delete/<user_id>", methods=['DELETE'])
    def delete_user(user_id):
        """"""
        db.user.delete_one({"_id": ObjectId(user_id)})

        flash("User deleted")
        return redirect(url_for("index"))

    return app
