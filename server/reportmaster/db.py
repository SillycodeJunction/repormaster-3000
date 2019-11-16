import pymysql.cursors
import os

from reportmaster.work_order import WorkOrder
from reportmaster.worker import Worker

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
        "(`status`, `data`, `category`, `hour_restrictions`, `owner_id`) "
        "VALUES (%(status)s,%(data)s,%(category)s,%(hour_restrictions)s,%(owner_id)s)"
    )
    return _insert_sql(sql, work_order.to_db())


def get_work_order_by_id(id):
    sql = "SELECT * FROM `work_order` WHERE id = %(id)s"
    data = _fetch_one(sql, dict(id=id))
    if not data:
        return None
    worker_id = data.get("worker_id", None)
    if worker_id:
        worker = get_worker_by_id(worker_id)
        return WorkOrder.from_db(data, worker)
    return WorkOrder.from_db(data)


def update_work_order_data(work_order):
    sql = "UPDATE `work_order` SET `data` = %(data)s WHERE id = %(id)s"
    _insert_sql(sql, work_order.to_db())


def update_work_order_status(work_order):
    sql = "UPDATE `work_order` SET `status` = %(status)s WHERE id = %(id)s"
    _insert_sql(sql, work_order.to_db())


def add_worker(worker):
    sql = "INSERT INTO `worker` (`name`, `role`) VALUES (%(name)s,%(role)s)"
    return _insert_sql(sql, worker.dict())


def get_worker_by_id(id):
    sql = "SELECT * FROM `worker` WHERE id = %(id)s"
    data = _fetch_one(sql, dict(id=id))
    if not data:
        return None
    return Worker(**data)


def get_work_orders_by_owner(owner):
    sql = "SELECT * FROM `work_order` WHERE owner_id = %(owner)s"
    data = _fetch_all(sql, dict(owner=owner))
    if not data:
        return None
    return [WorkOrder.from_db(d) for d in data]


def assign_worker(order_id, worker_id):
    sql = "UPDATE `work_order` SET `worker_id` = %(worker_id)s WHERE id = %(order_id)s"
    _insert_sql(sql, dict(order_id=order_id, worker_id=worker_id))
    return get_work_order_by_id(order_id)


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


def _fetch_all(sql, data):
    connection = _connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, data)
            return cursor.fetchall()
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
