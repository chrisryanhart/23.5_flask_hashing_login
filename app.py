from crypt import methods
from email.mime import image
from flask import Flask, request, redirect, render_template
from sqlalchemy import false
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddUserForm
from secrets import API_SECRET_KEY

git update test

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
# app.config['SQLALCHEMY_ECHO'] = True


# app.debug = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


# toolbar = DebugToolbarExtension(app)

# make postgres DB with name below

# connect_db(app)
# db.create_all()
