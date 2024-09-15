from flask import Blueprint, render_template  # Add render_template here

landing_bp = Blueprint('landing', __name__)

@landing_bp.route('/')
def home():
    return render_template('temp.html')
