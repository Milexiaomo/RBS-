from flask import Blueprint,render_template

user_set=Blueprint("user_set",__name__)

@user_set.route("/login/")
def user_login():
    return render_template("user_templates/login.html")
