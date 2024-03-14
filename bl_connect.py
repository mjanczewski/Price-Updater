"""Moduł do połączenia z Baselinker."""
import os
import requests
from dotenv import load_dotenv
import db_connect1


class BaselinkerConnect:
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv("BL_TOKEN")
        self.get_orders_from_baselinker()

    def get_orders_from_baselinker(self) -> "DataFrame":
        """
        Metoda pobiera zamówienia z Baselinker od numeru pobranego metodą 'get_last_order_id' z modułu db_connect
        """
        # TODO pobranie ostatniego zamówienia za pomoca metody get_last_order_id
        print("start get_orders_from_baselinker")
        last_order = db_connect1.DataBaseConnect()
        last_order = last_order.get_last_order_id()
        print(last_order)



abc = BaselinkerConnect()
