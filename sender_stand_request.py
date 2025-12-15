import configuration

import requests
import data

# Определение функции post_new_order для отправки post запроса на создание нового заказа
def post_new_order(body):
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers,
    )

# Определение функции get_order_by_track для отправки get запроса на получение заказа по треку заказа
def get_order_by_track(track):
    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track},
    )
