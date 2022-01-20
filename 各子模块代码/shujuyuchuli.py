import numpy as np
import pandas as pd
#打开数据库连接
import pymysql
import jieba
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
    n['cut']=n[0].apply(lambda x: list(jieba.cut(x)))
    n.head()
    n.columns=['content','mark','cut']
    print(n.head())
    stopwords=pd.read_csv('chineseStopWords.txt',encoding='gb18030',names=['stopword'],index_col=False)
    print(stopwords.head())
    stop_list=set(stopwords['stopword'])
    for i in n['cut']:
        for j in i:
            str(j)
            if j in stop_list:
                del j
    print(n.head())
    n.to_csv('cut.txt',columns=['cut','mark'],index=False)
    n.to_csv('cut1.csv',columns=['cut','mark'],encoding='gb18030')
    # 转成tsv格式
    file_path = "cut1.csv"
    text = pd.read_csv(file_path, sep=",",encoding='gb18030')
    text = text.sample(frac=1)  # 打乱数据集
    print(len(text))

    train = text[:int(len(text) * 0.8)]
    dev = text[int(len(text) * 0.8):int(len(text) * 0.9)]
    test = text[int(len(text) * 0.9):]

    train.to_csv('train.tsv', sep='\t', header=None, index=False, columns=None, mode="w")
    dev.to_csv('dev.tsv', sep='\t', header=None, index=False, columns=None, mode="w")
    test.to_csv('test.tsv', sep='\t', header=None, index=False, columns=None, mode="w")

    # 验证train,dev,test标签分布是否均匀
    for file in ['train', 'dev', 'test']:
        file_path = f"{file}.tsv"
        text = pd.read_csv(file_path, sep="\t", header=None)
        prob = dict()
        total = len(text[0])
        for i in text[0]:
            if prob.get(i) is None:
                prob[i] = 1
            else:
                prob[i] += 1
        # 按标签排序
        prob = {i[0]: round(i[1] / total, 3) for i in sorted(prob.items(), key=lambda k: k[0])}
        print(file, prob, total)
shujucunchu()