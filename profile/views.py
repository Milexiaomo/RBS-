from  flask import  Blueprint,render_template

profile=Blueprint("profile",__name__)

@profile.route("/update_profile/")
def update_profile():
    return render_template("reception/profile/update_profile.html")

