from flask import Blueprint, render_template, session, redirect

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    
    return render_template("dashboard.html")