import random

from bson.objectid import ObjectId
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_pymongo import PyMongo
from pymongo.errors import ServerSelectionTimeoutError

from webapp.forms import UserForm
from webapp.upload_user import get_user


def create_app(config: str = None):
    """Application factory

    :param config: configuration file
    """
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    mongo = PyMongo(app)
    db = mongo.db

    @app.route("/")
    def index():
        """Main page route endpoint.

        Connecting to db, check if it is empty.
        Uploads 1000 records if db is empty, using
        get_user function. Show existing records
        if not empty. Show lost connection flash
        if failed to connect to the db.

        :return render index.html template
        """
        try:
            users = db.users.find()
            if not users.count():
                db.users.insert_many(get_user(1000))
            return render_template("index.html", users=users)
        except ServerSelectionTimeoutError:
            users = []
            flash("Lost connection to database")
            return render_template("index.html", users=users)

    @app.route("/upload", methods=["POST"])
    def upload():
        """Uploads data from external API.

        Uploads number of records received from UI in
        POST request, using get_user function.

        :return redirect to index.html
        """
        num = request.form["number"]
        user = get_user(num)
        if user:
            db.users.insert_many(user)
            flash("Successfully added")
        else:
            flash("Upload failed")
        return redirect(url_for("index"))

    @app.route("/user/<user_id>")
    def user_profile(user_id: str):
        """Selects user from db by id.

        :param user_id: unique record id
        :return render user.html template
        """
        user = db.users.find_one_or_404({"_id": ObjectId(user_id)})
        return render_template("user.html", user=user)

    @app.route("/user/new", methods=["POST", "GET"])
    def new_user():
        """New user route endpoint.

        Render form for custom record. Check uniqueness
        by email field.

        :return render user.html template if success
        """
        form = UserForm()
        if form.validate_on_submit():
            data = {
                "name": {"first": form.first_name.data, "last": form.last_name.data},
                "gender": form.gender.data,
                "cell": form.phone.data,
                "email": form.email.data,
                "location": {
                    "city": form.city.data,
                    "country": form.country.data,
                    "street": {"name": form.street.data},
                },
                "picture": {"large": form.picture.data},
            }
            user = db.users.find_one({"email": form.email.data})
            if not user:
                db.users.insert_one(data)
                flash("Successfully added")
                user = db.users.find_one_or_404({"email": form.email.data})
                return render_template("user.html", user=user)
            flash("User with that email already exist")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(
                        "Mistake in field '{}': {}".format(
                            getattr(form, field).label.text, error
                        )
                    )
        return render_template("new_user.html", form=form)

    @app.route("/update_user/<user_id>", methods=["POST", "GET"])
    def update_user(user_id: str):
        """Update user route endpoint.
        Updated user info and render user.html
        template in case of success.

        :param user_id: unique record id
        :return  render user.html template
        """
        form = UserForm()
        if form.validate_on_submit():
            data = {
                "name": {"first": form.first_name.data, "last": form.last_name.data},
                "gender": form.gender.data,
                "cell": form.phone.data,
                "email": form.email.data,
                "location": {
                    "city": form.city.data,
                    "country": form.country.data,
                    "street": {"name": form.street.data},
                },
                "picture": {"large": form.picture.data},
            }
            db.users.find_one_and_replace({"_id": ObjectId(user_id)}, data)
            flash("Successfully added")
            user = db.users.find_one_or_404({"_id": ObjectId(user_id)})
            return render_template("user.html", user=user)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(
                        "Mistake in field '{}': {}".format(
                            getattr(form, field).label.text, error
                        )
                    )
        user = db.users.find_one_or_404({"_id": ObjectId(user_id)})
        return render_template("update_user.html", user=user, form=form)

    @app.route("/random")
    def random_user():
        """Chooses random record from database.

        :return render user.html or redirect to main page,
        if failed to get random user
        """
        users = db.users.find()
        if users:
            user = random.choice([user for user in users])
            return render_template("user.html", user=user)
        flash("Failed to get random user")
        return redirect(url_for("index"))

    @app.route("/delete/<user_id>", methods=["GET"])
    def delete_user(user_id: str):
        """Deletes record from database.

        :param user_id: unique records id
        :return redirect to main page after deletion
        """
        db.users.delete_one({"_id": ObjectId(user_id)})
        flash("User deleted")
        return redirect(url_for("index"))

    return app
