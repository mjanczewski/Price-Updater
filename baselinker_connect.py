"""Moduł do połączenia z Baselinker."""
import os
import requests
from dotenv import load_dotenv
import database_connect


class BaselinkerConnect:
    last_order_id = ""
    get_orders = "getOrders"
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv("BL_TOKEN")
        self.URL = os.getenv("BL_URL")
        self.get_orders_from_baselinker()

    # @staticmethod
    def get_orders_from_baselinker(self) -> "DataFrame":
        """
        Metoda pobiera zamówienia z Baselinker od numeru pobranego metodą 'get_last_order_id' z modułu db_connect
        """
        # TODO pobranie ostatniego zamówienia za pomoca metody get_last_order_id
        last_order = database_connect.DataBaseConnect()
        last_order_id = last_order.get_last_order_id()
        print(last_order_id)
        data = {"token": self.TOKEN, "method": self.get_orders }

        baselinker_response = requests.post(self.URL, data=data)

        print(baselinker_response.json())


abc = BaselinkerConnect()
