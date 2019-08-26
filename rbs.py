from  flask import  Flask,render_template,request,session,redirect,url_for
from  profile.views import profile
from user.views import user
from Tool.tool_db import DB
from datetime import datetime

app=Flask(__name__,static_url_path="")
app.debug=True
app.secret_key="fdsafh1232lk**(&*&%^&*"
app.register_blueprint(profile,url_prefix="/profile")
app.register_blueprint(user,url_prefix="/user")

@app.route("/")
def index():
    if session.get("username",None):
        sql = "select name,birthdate,address,email,phone,freelance,profile_title,profile_content from personal where name=?"
        name = session["username"][0][0]
        datas = DB.query_sql(sql, (name,),single_strip=True)
        datas=list(datas)
        datas[1]=int(datetime.now().year)-int(datas[1][0:4])
        return render_template("/reception/profile/index-2.html", datas=datas)
    else:
        return redirect(url_for("user.user_login"))


if  __name__=="__main__":
    app.run()
