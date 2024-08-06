import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="weatherreport",
        user="hao",
        password="1234"
    )
    print("連接成功!")
    conn.close()
except psycopg2.Error as e:
    print("連接失敗:", e)   