"""Moduł do połączenia z Baselinker."""
import os
import requests
from dotenv import load_dotenv

class BaselinkerConnect:
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv("BL_TOKEN")

    
    def get_orders_from_baselinker(self, last_order_id: 'str') -> 'DataFrame':
        """
        Metoda pobiera zamówienia z Baselinker od numeru pobranego metodą 'get_last_order_id' z modułu db_connect
        """
        # TODO pobranie ostatniego zamówienia za pomoca metody get_last_order_id
        pass

