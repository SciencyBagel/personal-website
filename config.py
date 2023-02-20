import os


class Database:
    CONNECTION_STRING: str = os.environ["CONNECTION_STRING"]


class Email:
    PORT = 465
    ID = os.environ["EMAIL"]
    PASSWORD = os.environ["PASSWORD"]


class Host:
    HOST = "0.0.0.0"
    PORT = 5000
