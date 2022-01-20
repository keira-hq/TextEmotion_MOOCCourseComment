import numpy as np
import pandas as pd
#打开数据库连接
import pymysql

def shujucunchu():
    db = pymysql.connect(host="localhost", user="root", password="123456", db="mooc")
    # 用cursor创建一个游标对象
    cur = db.cursor()
    # sql操作
    sql = "select content,mark from mooc_value"
    # 用execute实现sql操作
    cur.execute(sql)
    # 获取操作全部数据，保存在二维元祖results中
    results = cur.fetchall()
    # 描述结果列
    des = cur.description
    print("表的描述", des)
    # 显示表头
    print("表头：", ",".join([item[0] for item in des]))
    # n = np.array(results)
    n = pd.DataFrame(results)  # DataFrame是python中的pandas库中的一种数据结构，类似于excel，是一种二维表
    n.to_csv('result.csv')
shujucunchu()