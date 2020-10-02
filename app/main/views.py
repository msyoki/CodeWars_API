from . import main
from flask import render_template,url_for,flash,redirect,abort,request
from ..models import User,Post,Comment
from .forms import UpdateProfile,PostForm,CommentForm
from flask_login import login_required,current_user
from datetime import datetime
from .. import db
import requests
from ..models import Challenge
from ..requests import get_challenges



@main.route('/')
def home():
    title= 'Home - Codewars API '
    return render_template('index.html',title=title)

@main.route('/challenges', methods=['GET','POST'])
@login_required
def challenges():
    r = requests.get('https://www.codewars.com/api/v1/code-challenges/:slug={}?access_key={}')

    multiples=get_challenges('multiples-of-3-and-5')
    print(multiples)

    return render_template('challenges.html', multiples=multiples)

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts_count = Post.count_posts(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts = posts_count,date = user_joined)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        post = post_form.text.data
        category = post_form.category.data

        # Updated post instance
        new_post = Post(post_title=title,post_content=post,category=category,user=current_user,likes=0,dislikes=0)

        # Save post method
        new_post.save_post()
        return redirect(url_for('.home'))

    title = 'New post'
    return render_template('new_post.html',title = title,post_form=post_form )


@main.route('/posts/fashion_posts')
def leaderboard_climbers():

    posts = Post.get_posts('leaderboard_climbers')

    return render_template("lc_posts.html", posts = posts)

@main.route('/post/lifestyle_posts')
def highest_and_lowest():

    posts = Post.get_posts('highest_and_lowest')

    return render_template("hal_posts.html", posts = posts)

@main.route('/posts/travel_posts')
def two_oldest_ages():

    posts = Post.get_posts('two_oldest_ages')

    return render_template("toa_posts.html", posts = posts)




@main.route('/post/<int:id>', methods = ['GET','POST'])
def post(id):
    post = Post.get_post(id)
    posted_date = post.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        post.likes = post.likes + 1

        db.session.add(post)
        db.session.commit()

        return redirect("/post/{post_id}".format(post_id=post.id))

    elif request.args.get("dislike"):
        post.dislikes = post.dislikes + 1

        db.session.add(post)
        db.session.commit()

        return redirect("/post/{post_id}".format(post_id=post.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,post_id = post)

        new_comment.save_comment()


    comments = Comment.get_comments(post)

    return render_template("post.html", post = post, comment_form = comment_form, comments = comments, date = posted_date)

@main.route('/user/<uname>/posts')
def user_posts(uname):
    user = User.query.filter_by(username=uname).first()
    posts = Post.query.filter_by(user_id = user.id).all()
    posts_count = Post.count_posts(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/posts.html", user=user,posts=posts,posts_count=posts_count,date = user_joined)
