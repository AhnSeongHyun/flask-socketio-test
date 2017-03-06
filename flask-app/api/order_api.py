# -*- coding:utf-8 -*-
from flask import Blueprint, request
import requests

order_api = Blueprint('api', __name__, url_prefix='/api')


@order_api.route('/order', methods=['POST'])
def test_api_order():
    order_num = request.form.get('order_num', 'NULL')
    NOTIFY_URL = "http://localhost:5001/order/notify"
    r = requests.get(NOTIFY_URL + "/" + str(order_num))
    return "TEST INSERT ORDER : " + str(order_num) + "   SocketIO RES : " + str(r.status_code)