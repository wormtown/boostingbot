#AuthRoutes.py

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return 'Login page'

@auth_bp.route('/logout')
def logout():
    return 'Logout page'

@auth_bp.app_errorhandler(404)
def not_found_error(error):
    return '404 Not Found', 404

