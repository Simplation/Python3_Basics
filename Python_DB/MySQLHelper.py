#!/usr/bin/env python
# encoding: utf-8
"""
@file: MySQLHelper.py
@time: 2018-09-27 17:43
@desc: 封装 Mysql 用法
"""

import pymysql


class MySQLHelper(object):

    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    db=self.db,
                                    user=self.user,
                                    passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sqls, params=()):
        results = None
        try:
            self.cursor.execute(sqls, params)
            results = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)

        return results

    def get_all(self, sqls, params=()):
        lists = ()
        try:
            self.cursor.execute(sqls, params)
            lists = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)

        return lists

    def insert(self, sqls, params=()):
        return self.__edit(sqls, params)

    def update(self, sqls, params=()):
        return self.__edit(sqls, params)

    def delete(self, sqls, params=()):
        return self.__edit(sqls, params)

    def __edit(self, sqls, params):
        count = 0
        try:
            count = self.cursor.execute(sqls, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)

        return count


if __name__ == '__main__':
    helper = MySQLHelper('IP',
                         3306,
                         'USER',
                         'PASSWORD',
                         'DB')

    sql = "SELECT * FROM 表名"

    result = helper.get_all(sql)
    print(result)
