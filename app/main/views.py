from flask import render_template,request,redirect,url_for
from . import main
from .requests import get_news,get_articles
from .models import News    