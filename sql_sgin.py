import pymysql
from typing import Tuple, Any
import datetime


# 增
def data_insert(data: Tuple[str, ...]) -> str:
    d = pymysql.connect(user='root', host='127.0.0.1', password='3779404', database='bases_sing')
    self_id, self_name = data
    cursor = d.cursor()
    sql = fr"insert into sing values('{self_id}', '{self_name}', 0, '1942-1-1');"
    cursor.execute(sql)
    d.commit()
    d.close()
    return '创建成功,请再次签到'


# 改
def data_update(data: Tuple[str, ...]) -> str:
    d = pymysql.connect(user='root', host='127.0.0.1', password='3779404', database='bases_sing')
    date_time = datetime.datetime.now().strftime('%Y-%m-%d')
    user_id, fraction = data
    cursor = d.cursor()
    sql = fr"""update sing set sing_freaction=sing_freaction+{fraction},  sing_date='{date_time}' where user_id={user_id}; """
    cursor.execute(sql)
    d.commit()
    d.close()
    return '签到成功'


# 查
def data_select(self_id: str) -> Tuple[Any]:
    d = pymysql.connect(user='root', host='127.0.0.1', password='3779404', database='bases_sing')
    cursor = d.cursor()
    sql = fr"""select * from sing where user_id={self_id};"""
    cursor.execute(sql)
    da = cursor.fetchall()
    d.close()
    if da == ():
        dat = None
    else:
        dat = da[0]
    return dat


# # 删
def data_delete(data: str) -> str:
    d = pymysql.connect(user='root', host='127.0.0.1', password='3779404', database='bases_sing')
    cursor = d.cursor()
    # user_id, user_name, fraction, date_time = data
    sql = fr"""delete from sing where user_id={data};"""
    cursor.execute(sql)
    d.commit()
    d.close()
    return "删除成功"


if __name__ == '__main__':
    # print(data_update(('2174188197', '100')))
    print(data_select(('2174188197')))
    print(data_delete('3277806172'))
