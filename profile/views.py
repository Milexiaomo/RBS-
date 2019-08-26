from  flask import  Blueprint,render_template,request,redirect,url_for,session,send_from_directory
from datetime import datetime
from Tool.tool_db import DB
import os

profile=Blueprint("profile",__name__)
UPLOAD_FOLDER=r".\uploads\header_title"
ALLOWED_EXTENSIONS=[".jpg",'.png','.gif']

#呈现特定目录下的资源
@profile.route("/head_portrait/<filename>")
def header_portrait(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)

#检查文件是否允许上传
def allowed_file(filename):
    name,ext=os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS

@profile.route("/update_profile/")
def update_profile():
    sql="select head_portrait,name,birthdate,address,email,phone,freelance,profile_title,profile_content from personal where name=?;"
    username=session["username"][0][0]
    datas=DB.query_sql(sql,(username,),single_strip=True)
    return render_template("reception/profile/update_profile.html",datas=datas)

#提交修改请求
@profile.route("/submit_profile/",methods=["POST"])
def submit_profile():
    header_png=None
    if  "header_png" in request.files:
        header_png=request.files["header_png"]
        if allowed_file(header_png.filename):
            img_path=datetime.now().strftime("%Y%m%d%H%M%f")+os.path.splitext(header_png.filename)[1]
            header_png.save(os.path.join(UPLOAD_FOLDER,img_path))
    username=request.form["username"]
    birthdate=datetime(int(request.form['year']),int(request.form['month']),int(request.form['days'])).date()
    address=request.form.get('address')
    email=request.form.get('email')
    phone=request.form.get('phone')
    freelance=request.form.get('freelance')
    profile_title=request.form.get('profile-title')
    profile_content=request.form.get('profile-text')
    sql="update personal set name=?,birthdate=?,address=?,email=?,phone=?,freelance=?,profile_title=?,profile_content=? ,head_portrait=? where rowid=2;"
    DB.execute_sql(sql,(username,birthdate,address,email,phone,freelance,profile_title,profile_content,img_path))
    return redirect(url_for("index"))


    