from flask import Blueprint,render_template

bowler = Blueprint('bowler',__name__)

@bowler.route("/bowler", methods=["GET"])
def bowl1():
    return render_template('bowler.html')