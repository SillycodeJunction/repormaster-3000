import pymysql.cursors
import os

from reportmaster.work_order import WorkOrder

DB_PASSWORD = os.environ.get("DB_PASSWORD", "mysql")
DB_HOST = os.environ.get("DB_HOST", "localhost")


def create_work_order(work_order):
    """
    Create work order, returns the id of the created order
    :param work_order:
    :return:
    """
    sql = (
        "INSERT INTO `work_order` "
        "(`status`, `data`, `category`, `hour_restrictions`) "
        "VALUES (%(status)s,%(data)s,%(category)s,%(hour_restrictions)s)"
    )
    return _insert_sql(sql, work_order.to_db())


def get_work_order_by_id(id):
    sql = "SELECT * FROM `work_order` WHERE id = %(id)s"
    print(f"FETCHING ID {id}")
    data = _fetch_one(sql, dict(id=id))
    if not data:
        return None
    print(f"{data}")
    return WorkOrder.from_db(data)


def update_work_order_data(work_order):
    sql = "UPDATE `work_order` SET `data` = `%(data)s` WHERE id = %(id)s"
    _insert_sql(sql, work_order.to_db())


def _insert_sql(sql, data):
    connection = _connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, data)
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()


def _fetch_one(sql, data):
    connection = _connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, data)
            return cursor.fetchone()
    finally:
        connection.close()


def _connect():
    return pymysql.connect(
        host=DB_HOST,
        user="root",
        password=DB_PASSWORD,
        db="reportmaster",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
