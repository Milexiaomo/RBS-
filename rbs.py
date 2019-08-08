from  flask import  Flask,render_template
from  profile.views import profile

app=Flask(__name__,static_url_path="")
app.debug=True

app.register_blueprint(profile,url_prefix="/profile")

@app.route("/")
def index():
    return render_template("reception/profile/index-2.html")


if  __name__=="__main__":
    app.run()
