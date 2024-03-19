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

        data = {"token": self.TOKEN, "method": self.get_orders}

        baselinker_response = requests.post(self.URL, data=data).json()

        for i in range(len(baselinker_response["orders"])):
            number_of_products = len(baselinker_response["orders"][i]["products"])
            last_order_in_baselinker = baselinker_response["orders"][i]["orders_id"]
            for j in range(number_of_products):
                if baselinker_response["orders"][i]["admin_comments"] != "":
                    bl_order_id = baselinker_response["orders"][i]["order_id"]
                    bl_admin_comment = baselinker_response["orders"][i]["admin_comments"]
                    bl_user_login = baselinker_response["orders"][i]["user_login"]
                    bl_user_fullname = baselinker_response["orders"][i]["delivery_fullname"]
                    bl_sku = baselinker_response["orders"][i]["products"][j]["sku"]


    def get_invoices_number_from_baselinker(self):
        pass


get_orders_info = BaselinkerConnect()
get_orders_info.get_orders_from_baselinker()
