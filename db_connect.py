"""Moduł do połączenia z bazą dancyh."""

import pypyodbc as odbc


class DataBaseConnect:
    SERVER = "LAPTOP-EK"
    DATABASE = "SN_Downloader"
    CONNECTION_STRING = odbc.connect(
        Trusted_Connection="Yes",
        Driver="{SQL SERVER}",
        Server=f"{SERVER}",
        Database=f"{DATABASE}",
    )

    def get_last_order_id(self) -> 'str':
        """
        Metoda pobierająca ostatni numer zamówienia z bazy danych
        -> string
        """
        last_order = ""
        cursor = self.CONNECTION_STRING.cursor()
        last_order_id = list(cursor.execute(f"SELECT LastOrderId FROM SN_Downloader.dbo.LastOrderId"))
        for row in last_order_id:
            last_order = str(row[0])

        cursor.close()
        print(last_order)
        return last_order

    def set_last_order_id(self, last_order_id: 'str'):
        """
        Metoda ustawiająca ostatni numer zamówienia w bazie danych
        """
        self.last_order_id = last_order_id
        cursor = self.CONNECTION_STRING.cursor()
        cursor.execute(f"UPDATE LastOrderId SET LastOrderId={self.last_order_id}")
        cursor.commit()
        cursor.close()


# connect = DataBaseConnect()
# connect.get_last_order_id()
# connect.set_last_order_id("12")
# connect.get_last_order_id()
