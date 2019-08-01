from  flask import  Flask,render_template
from user.views import user_profile
app=Flask(__name__,static_url_path="")
app.debug=True

app.register_blueprint(user_profile,url_prefix="/user")

@app.route("/")
def index():
    return render_template("reception/index-2.html")


if  __name__=="__main__":
    app.run()
