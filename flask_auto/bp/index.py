

from flask import Blueprint,render_template


from flask_auto.utils.tokenrequired import token_required


index_blueprint =Blueprint("index_blueprint",__name__,url_prefix="/")


@index_blueprint.route("/")
@token_required
def index(current_user):
    return render_template("index.html")