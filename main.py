from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(480))

    def __init__(self, title, body):
        self.title = title
        self.body = body
    def __repr__(self):
        return '<Post Title: %r>' % self.title

#Shows all blog posts
@app.route("/blog")

#Allows user to make new blogpost   
@app.route("newpost")

@app.route("/")