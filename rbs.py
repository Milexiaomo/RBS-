from  flask import  Flask,render_template

app=Flask(__name__,static_url_path="")
app.debug=True

@app.route("/")
def index():
    return render_template("reception/index-2.html")

@app.route("/reception/blog/")
def reception_blog():
    return render_template("reception/blog.html")

@app.route("/reception/base/")
def blog():
    return render_template("reception/base.html")

@app.route("/blog/post/")
def  blog_post():
    return render_template("reception/blog-post.html")

@app.route('/blog_backstage/')
def  blog_ba():
    return render_template("backstage/index.html")


if  __name__=="__main__":
    app.run()
