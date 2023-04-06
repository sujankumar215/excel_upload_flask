from flask import Blueprint,render_template

batsman = Blueprint('batsman',__name__,template_folder='templates')

@batsman.route("/batsman", methods=["GET"])
def bat():
    return render_template('batsman.html')
