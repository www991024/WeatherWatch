from fastapi import FastAPI
from db_connect import get_connection
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


conn = get_connection()

if conn:
    try:
        # 创建游标对象
        cur = conn.cursor()

        # 执行查询
        cur.execute("SELECT * FROM mytable;")
        rows = cur.fetchall()

        # 处理结果
        for row in rows:
            print(row)

        # 关闭游标和连接
        cur.close()
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        conn.close()