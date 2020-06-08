from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, login_user, logout_user, current_user

from devconnect.models import Post, Comment, db
from config import Config
from devconnect.view_post import bp
from devconnect.view_post.forms import CommentForm, ReplyForm

@bp.route('/post/<postid>', methods=['GET', 'POST'])
@login_required
def view_post(postid):
    commentform = CommentForm()
    replyform = ReplyForm()

    if commentform.validate_on_submit():
        new_comment = Comment(
            body=commentform.body.data,
            author=current_user,
            post=Post.query.get(postid)
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect('/post/'+postid)

    if replyform.submit.data:
        parent = Comment.query.get(replyform.parentid.data)
        new_subcom = Comment(
            body=replyform.body.data,
            author=current_user,
            post=Post.query.get(postid),
            parent=parent
        )

        db.session.add(new_subcom)
        db.session.commit()

        return redirect('/post/'+postid)
    


    post = Post.query.get(postid)
    return render_template('post.html', post=post, commentform=commentform, replyform=replyform)
