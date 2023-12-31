from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import User, Post
from . import db
from flask import session, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    posts = Post.query.filter_by(published=True).order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    user = User.query.get(user_id)
    # Check if the logged-in user is 'pythonadmin'
    is_root_user = user and user.username == 'pythonadmin'

    # Fetch all posts ordered by date (latest first)
    all_posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('dashboard.html', all_posts=all_posts)


#Add Post Route
@main_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = session.get('user_id')

        # Create new Post object
        new_post = Post(title=title, content=content, author_id=user_id)
        # Add to database and commit
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    return render_template('add-post.html')

#Edit Post Route:

@main_bp.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    return render_template('edit-post.html', post=post)

#Delete Post Route:

@main_bp.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
