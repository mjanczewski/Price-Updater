"""Moduł do połączenia z bazą dancyh."""

import pypyodbc as odbc


class DataBaseConnect:
    __SERVER = "LAPTOP-EK"
    __DATABASE = "SN_Downloader"
    __CONNECTION_STRING = odbc.connect(
        Trusted_Connection="Yes",
        Driver="{SQL SERVER}",
        Server="Laptop-EK",
        Databas="SN_Downloader",
    )

    def get_last_order_id(self) -> 'str':
        """
        Metoda pobierająca ostatni numer zamówienia z DB
        -> string
        """
        last_order = ""
        cursor = self.__CONNECTION_STRING.cursor()
        last_order_id = list(cursor.execute(f"SELECT LastOrderId FROM SN_Downloader.dbo.LastOrderId"))
        for row in last_order_id:
            last_order = str(row[0])
            # return str(row[0])

        print(last_order)
        return last_order


connect = DataBaseConnect()
connect.get_last_order_id()
