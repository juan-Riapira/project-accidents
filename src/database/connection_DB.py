import cx_Oracle

def get_db_connection():
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")

        connection = cx_Oracle.connect(
            user="bibian",
            password="2024",
            dsn=dsn
        )
        return connection
   