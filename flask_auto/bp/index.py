

from flask import Blueprint,render_template,redirect


from flask_auto.utils.tokenrequired import token_required


index_blueprint =Blueprint("index_blueprint",__name__,url_prefix="/")


@index_blueprint.route("/")
def index():
    return render_template("index.html")




