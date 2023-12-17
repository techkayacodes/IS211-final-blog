from flask import (
    Blueprint, render_template, redirect, request,
    url_for, flash, session
)
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from . import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')  # Use prefix if needed

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            # Redirect to the dashboard page after a successful login
            return redirect(url_for('main.dashboard'))
        
        # Flash message for invalid credentials
        flash('Invalid username or password')
    
    # Render the login template
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    # Remove the user_id from the session to log the user out
    session.pop('user_id', None)
    # Redirect to the index page after logout
    return redirect(url_for('main.index'))

@auth_bp.route('/create_user', methods=['GET', 'POST'])
def create_user():
    # Only allow creating new users if the root user is logged in
    if not session.get('user_id') == User.query.filter_by(username='pythonadmin').first().id:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('New user created successfully!')
        return redirect(url_for('auth.login'))
    
    return render_template('create_user.html')