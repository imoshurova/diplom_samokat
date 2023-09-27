# Ирина Ярошук, 8а когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Тест
def test_get_order_by_track():
   resp_get_order = sender_stand_request.get_order_by_track()
   # Проверить, что код ответа равен 200
   assert resp_get_order.status_code == 200