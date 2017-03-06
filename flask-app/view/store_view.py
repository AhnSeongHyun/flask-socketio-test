# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
import requests

store_view = Blueprint('store_view', __name__, url_prefix='/')


@store_view.route('/', methods=['GET'])
def index():
    return render_template("index.html")