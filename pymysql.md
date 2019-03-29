## 1、MySQL 安装

- 1.1、下载 MySQL

​    官网：<https://dev.mysql.com/downloads/mysql/> 选择对应版本下载即可

- 1.2、安装

​    安装步骤就不在这里赘述。



## 2、MySQL 数据库连接，并实现增删改查等操作

​    注意：首先需要需要进行 import 操作

- 2.1、创建表操作(数据库相同的表明只能创建一次，多次创建会报错)

```
import pymysql 

# 创建表的操作 
def create_table():  

     # 连接数据库     
     db = pymysql.connect(host='localhost’,
                          user='root',                          
                          password='wangzhao',                          
                          db=‘test'
                          )     

     sql = '''create table if not exists department (
                             id int NOT NULL AUTO_INCREMENT, 
                             name text,              
                             sex text,              
                             salary float,              
                             PRIMARY KEY (`id`)              
                             )'’’ 

     

     # 使用 cursor() 创建 cursor 对象    
     cursor = db.cursor()     

     try:         
         # 执行 sql 语句的操作         
         cursor.execute(sql)     

         # 提交数据库的操作         
         db.commit()       
         print('create db success.')   

     except BaseException as e: 
         # 如果发生意外，则进行回滚操作         
         db.rollback()         
         print(e)     

     finally:         
         # 关闭游标和数据库         
         cursor.close()         
         db.close()

```

- 2.2、添加数据库操作

```
import pymysql

# 插入数据库的操作 
def insert_table(): 
     # 连接数据库     
     db = pymysql.connect(host='localhost’,
                           user='root',
                           password='wangzhao',
                           db='test',
                           charset="utf8")

     print('数据库连接成功.’) 
     

     # sql 语句     
     sql = 'insert into department (name, sex, salary) values(%s, %s, %s)’

     # 使用 cursor() 创建 cursor 对象     
     cursor = db.cursor()  

     try:         
         # 创建要插入的值         
         values = ('李晨阳', '男', 9000)         

         # 执行 sql 语句         
         cursor.execute(sql, values)         

         # 提交数据库操作         
         db.commit()         
         print('insert db success.')     

     except BaseException as e:         
         # 出现意外则进行回滚操作         
         db.rollback()        
         print(e)    

     finally:         
         # 关闭游标和数据库         
         cursor.close()         
         db.close()

```



- 2.3、修改数据库操作

```
import pymysql

# 修改数据库的操作
def update_table():
      db = pymysql.connect(host='localhost’,
                           user='root’,
                           password='wangzhao’, 
                           db='test’,
                           charset='utf8’)


      print('数据库连接成功.’)

      sql = 'update department set name=%s, sex=%s, salary=%s where id = 2’

      # 创建 cursor 对象
      cursor = db.cursor()

      try:
          values = ('John', '男', 7500)

          # 执行 sql 语句
          cursor.execute(sql, values)

          # 提交数据库操作
          db.commit()
          print('update db success.’)

      except BaseException as e:

          # 出现异常则进行回滚操作
          db.rollback()
          print(e)

      finally:
          # 关闭游标和数据库
          cursor.close()
          db.close()
```



- 2.4、查询数据库操作

```
import pymysql

# 查询数据库的操作
def query_table():
      db = pymysql.connect(host='localhost’,
                           user='root’,
                           password='wangzhao’,
                           db='test’,
                           charset='utf8’)

      print('连接数据库成功.’)

      sql = 'select * from department’
      cursor = db.cursor()

      try:

          # 执行 sql 语句
          cursor.execute(sql)

          # 查询一条记录
          result = cursor.fetchone()
          print('查询到的一条记录是: id=%s name=%s, sex=%s, salary=%d' % (result[0], result[1], result[2], result[3]))

          # 如果先⽤ fetchone()，游标是从 1 开始
          # 重置游标位置，偏移量:⼤于0向后移动;⼩于0向前移动，mode默认是relative
          # relative:表示从当前所在的⾏开始移动; absolute:表示从第⼀⾏开始移动
          cursor.scroll(0, mode='absolute’)


          # 查询多条语句
          results = cursor.fetchall()

          for result in results:
              print('查询到的记录是：id=%s, name=%s, sex=%s, salary=%s' % (result[0], result[1], result[2], result[3]))
          print('query db success.’)

      except  BaseException as e:

          # 出现异常则进行回滚操作
          db.rollback()
          print(e)

      finally:

          # 关闭游标和数据库
          cursor.close()
          db.close()


```



- 2.5、删除数据库操作

```
import pymysql

# 删除数据库的操作
def delete_table():
      db = pymysql.connect(host='localhost’,
                           user='root’,
                           password='wangzhao’,
                           db='test’)

      print('db connect success.’)

      sql = 'delete from department where id=%s’
      cursor = db.cursor()

      try:

          # 执行 sql 语句
          cursor.execute(sql, 5)
          db.commit()
          print('delete db success.’)

      except BaseException as e:

          # 出现异常则进行回滚操作
          db.rollback()
          print(e)


      finally:
          # 关闭游标和数据库
          cursor.close()
          db.close()
```

