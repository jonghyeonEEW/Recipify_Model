import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       charset='utf8')

with conn:
    with conn.cursor() as cur:
        cur.execute('CREATE DATABASE mydb')
        conn.commit()