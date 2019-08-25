from flask import Blueprint,render_template
from user.models import user_login


user=Blueprint("user",__name__)

user.add_url_rule("/login/",view_func=user_login.as_view("user_login"))


