from flask import Blueprint,render_template
from user.models import Personal


user_profile=Blueprint("user_profile",__name__)

@user_profile.route("/profile/")
def profile():
    p=Personal()
    datas=p.personal_data()
    return render_template("backstage/index.html",datas=datas)

