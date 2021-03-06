from flask.views import MethodView
from Tool.tool_db import DB
from flask import render_template,request,session,redirect,url_for,flash

import sys
sys.path.append(r"F:\RBS")

class user_login(MethodView):
    def get(self):
        return render_template("/user_templates/login.html/")
    def post(self):
        email=request.form["email"]
        password=request.form["password"]
        sql="select count(*) from personal where email=? and password=? "
        num=DB.query_sql(sql,(email,password))
        if num[0][0]:
            sql="select name from personal where email=? and password=?"
            username=DB.query_sql(sql,(email,password))
            session["username"]=username
            return redirect(url_for("index"))
        else:
            flash("您输入的邮箱或密码错误")
            return render_template("/user_templates/login.html")
