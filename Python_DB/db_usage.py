#!/usr/bin/env python
# encoding: utf-8
import pymysql


class DB_Test(object):

    # 创建表
    def create_table(self):
        # 建立连接
        db = pymysql.Connect(host='localhost',
                             user='root',
                             password='password',
                             db='test',
                             charset='utf8')

        # 创建 developer 数据库的语句
        sql = """create table if not exists developer (
                 id int NOT NULL AUTO_INCREMENT,
                 name text,
                 job text,
                 site text,
                 PRIMARY KEY (`id`)
              )"""

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交事务
            db.commit()
            print('create table success.')
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            # 关闭游标和数据库
            cursor.close()
            db.close()

    def insert_table(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='test')

        # 插入操作的语句
        sql = 'insert into developer (name, job, site) values (%s, %s, %s)'

        # 使用 cursor() 创建一个 cursor 对象
        cursor = db.cursor()

        try:
            # 初始化数据库需要插入的值
            values = ('Simplation', 'Android Developer', 'www.android.com')

            # 执行
            cursor.execute(sql, values)
            # 提交
            db.commit()
            print('insert success')

        except BaseException as e:
            # 如果发生意外则进行回滚操作
            db.rollback()
            print(e)
        finally:
            # 关闭游标和数据库
            cursor.close()
            db.close()

    def query_table(self):
        # 链接数据库
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='test')

        sql = 'select * from developer'

        cursor = db.cursor()

        try:
            cursor.execute(sql)
            # 查询⼀条记录
            result = cursor.fetchone()
            print('查询⼀条记录：id=%s,name=%s,job=%s,site=%s' % (result[0], result[1], result[2], result[3]))
            # 如果先⽤ fetchone()，游标是从 1 开始
            # 重置游标位置，偏移量:⼤于0向后移动;⼩于0向前移动，mode默认是relative
            # relative:表示从当前所在的⾏开始移动; absolute:表示从第⼀⾏开始移动
            cursor.scroll(0, mode='absolute')
            # 查询多条记录
            results = cursor.fetchall()
            for row in results:
                print('查询多条记录：id=%s,name=%s,job=%s,site=%s' % (row[0], row[1], row[2], row[3]))
            print('query success.')
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            # 关闭数据库和游标
            cursor.close()
            db.close()

    def update_table(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='test')

        sql = 'update developer set name=%s, job=%s, site=%s'
        cursor = db.cursor()

        try:
            values = ('Simplation', 'Android', 'www.baidu.com')
            cursor.execute(sql, values)
            db.commit()
            print('update success.')
        except BaseException as e:
            db.rollback()
            print(e)
        finally:
            # 关闭游标和数据库
            cursor.close()
            db.close()

    def delete_table(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='test')

        sql = 'delete from developer where id=%s'

        cursor = db.cursor()

        try:
            cursor.execute(sql, 1)
            db.commit()
            print('delete success.')

        except BaseException as e:
            # 出现意外进行回滚操作
            db.rollback()
            # 打印错误
            print(e)
        finally:
            cursor.close()
            db.close()


if __name__ == "__main__":
    dateBase = DB_Test()
    dateBase.create_table()
    dateBase.insert_table()
    dateBase.query_table()
    dateBase.update_table()
    dateBase.delete_table()
