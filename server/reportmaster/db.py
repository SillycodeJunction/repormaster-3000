import pymysql.cursors
import os

DB_PASSWORD = os.environ.get("DB_PASSWORD", "mysql")

connection = pymysql.connect(host='localhost',
                             user='root',
                             password=DB_PASSWORD,
                             db='reportmaster',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `projects` (`status`, `description`) VALUES (%s, %s)"
        cursor.execute(sql, ('new', 'Some description'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `status`, `description` FROM `projects` WHERE `aindex`=%s"
        cursor.execute(sql, (1,))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
