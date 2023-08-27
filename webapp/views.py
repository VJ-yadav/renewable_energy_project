"""This File will contain all our website routes, that is supposed to be viewed
1. All the routes, except for login are here
"""
"""In Flask, a blueprint is a way to organize and structure your web application by breaking it into smaller, modular components."""
"""Blueprints help you manage routes, views, templates, and other application functionalities in a more organized and maintainable manner. """


from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")
