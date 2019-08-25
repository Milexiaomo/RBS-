from  flask import  Blueprint,render_template,request,redirect,url_for,session
from datetime import datetime
from Tool.tool_db import DB

profile=Blueprint("profile",__name__)

@profile.route("/update_profile/")
def update_profile():
    return render_template("reception/profile/update_profile.html")

@profile.route("/submit_profile/",methods=["GET"])
def submit_profile():
    username=request.args["username"]
    birthdate=datetime(int(request.args['year']),int(request.args['month']),int(request.args['days'])).date()
    address=request.args.get('address')
    email=request.args.get('email')
    phone=request.args.get('phone')
    freelance=request.args.get('freelance')
    profile_title=request.args.get('profile-title')
    profile_content=request.args.get('profile-text')
    sql="update personal set name=?,birthdate=?,address=?,email=?,phone=?,freelance=?,profile_title=?,profile_content=? where rowid=2;"
    DB.execute_sql(sql,(username,birthdate,address,email,phone,freelance,profile_title,profile_content))
    return redirect(url_for("index"))

@profile.route("/show_profile/")
def show_profile():
    sql="select name,birthdate,address,email,phone,freelance,profile_title,profile_content from personal where name=?"
    name=session["username"][0][0]
    datas=DB.query_sql(sql,(name,))
    return  render_template("/reception/profile/index-2.html",datas=datas)

    