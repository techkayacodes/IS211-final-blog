from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Post, User
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    posts = Post.query.filter_by(published=True).order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_posts = Post.query.filter_by(author_id=session['user_id']).order_by(Post.date_posted.desc()).all()
    return render_template('dashboard.html', posts=user_posts)

# Add more routes for add_post, edit_post, delete_post, etc.
