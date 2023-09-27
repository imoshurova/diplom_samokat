import data
import requests
import configuration

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=body, headers=data.headers)  # подставляем тело и заголовки
resp_order = post_new_order(data.order_body)
print(resp_order.status_code) #получаем код ответа
print(resp_order.json()) #получаем трек номер заказа


# Получение заказа по треку
def get_order_by_track():
        return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,  # подставялем полный url
                       params={"t": resp_order.json()["track"]})
resp = get_order_by_track()
print (resp.status_code)
