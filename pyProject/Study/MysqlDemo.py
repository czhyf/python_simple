import pymysql

def get_conn():
    host = 'localhost'
    user = 'root'
    password = 'Demo711604.'
    port = 3306
    db = pymysql.connect(host=host, user=user, password=password, port=port,db='spiders')
    return db
def create_table():
    cursor=get_conn().cursor()
    sql='create table if not exists students(id varchar(255) not null ,name varchar(255) not null ,age int not  null primary key )'
    cursor.execute(sql)
    cursor.close()
def insert_table():
    id='2012001'
    usr='Bob'
    age=20
    db=get_conn()
    cursor=db.cursor()
    sql='insert into students(id,name,age) values (%s,%s,%s)'
    try:
        cursor.execute(sql,(id,usr,age))
        db.commit()
    except:
        print(1)
        db.rollback()
    db.close()
def insert_table_2():
    pass

if __name__ == '__main__':
    pass
