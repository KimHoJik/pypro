# 원격 데이터베이스 연동
import MySQLdb

# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)    # dict 타입
    cursor = conn.cursor()
    """
    print('insert ---')
    # isql = "insert into sangdata(code,sang,su,dan) values(10,'신상',5,5000)"
    # isql = "insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)"
    isql = "insert into sangdata values(%s,%s,%s,%s)"
    sql_data = (10, '신상',5,5000)
    # sql_data = 10, '신상',5,5000
    cursor.execute(isql, sql_data)
    conn.commit()
    """
    """
    print('update ---')
    usql = "update sangdata set sang=%s,su=%s where code=%s"
    sql_data = ('얼죽아', 30, 10)
    cursor.execute(usql, sql_data)
    conn.commit()
    """
    
    print('delete ---')
    input_code = '10'
    # dsql = "delete from sangdata where code=" + input_code  # secure coding 가이드 라인에 위배
    # dsql = "delete from sangdata where code=%s"
    # cou = cursor.execute(dsql, (input_code,))
    dsql = "delete from sangdata where code='{}'".format(input_code)
    cou = cursor.execute(dsql)
    conn.commit()
    if cou > 0:
        print('삭제 성공')
    else:
        print('삭제 실패')
    
    
    print('select ---')
    sql = "select code,sang,su,dan from sangdata"
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        # print(data)
        print('%s %s %s %s'%data)
    
except Exception as e:
    print('error : ', e)
finally:
    cursor.close()
    conn.close()