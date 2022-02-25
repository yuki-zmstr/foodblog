from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user 
from .models import Comment
from flask_sqlalchemy import SQLAlchemy
from . import db
import json
import time


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    time.sleep(0.1)
    comments = db.session.query(Comment).all()
    print('doing something here')
    return render_template("home.html", user=current_user, comments=comments)

# @views.route('/processFoodInfo/<string:foodInfo>', methods=['POST'])
# def processFoodID(foodInfo):
#     print('making request here')
#     comments = db.session.query(Comment).all()
#     foodInfo = json.loads(foodInfo)
#     id = foodInfo['id']
#     comment = foodInfo['comment']
#     print('Food ID: ', id)
#     print('Comment: ', comment)
#     if len(comment) < 1:
#         print('Comment is too short!')
#     else:
#         # print('Im here!!!!!!!!!!!!!!!!!!')
#         new_comment = Comment(data=comment, user_id=current_user.id, food_id=id, user_name=current_user.first_name)
#         db.session.add(new_comment)
#         db.session.commit()
#         print(f'Comment added for {id}')
#     time.sleep(0.1)
#     comments = db.session.query(Comment).all()
#     # for c in comments:
#     #     print(c.data)
#     return render_template("home.html", user=current_user, comments=comments)

@views.route('/processFoodInfo', methods=['POST'])
def processFoodID():
    comments = db.session.query(Comment).all()
    foodInfo = json.loads(request.data)
    id = foodInfo['id']
    comment = foodInfo['comment']
    print('Food ID: ', id)
    print('Comment: ', comment)
    # checking of length of comment done on the front end.
    # if len(comment) < 1:
    #     print('Comment is too short!')
    # else:
    new_comment = Comment(data=comment, user_id=current_user.id, food_id=id, user_name=current_user.first_name)
    db.session.add(new_comment)
    db.session.commit()
    print(f'Comment added for {id}')
    time.sleep(0.1)
    comments = db.session.query(Comment).all()
    return render_template("home.html", user=current_user, comments=comments)

@views.route('/delete-comment', methods=['POST'])
def delete_comment():
    comment = json.loads(request.data)
    commentId = comment['commentId']
    comment = Comment.query.get(commentId)
    if comment:
        if comment.user_name == current_user.first_name or current_user.first_name == 'Admin':
            # admin can delete all comments.
            db.session.delete(comment)
            db.session.commit()
    return jsonify({})
