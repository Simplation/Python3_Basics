## Python 内置读写文件的函数，一般分为三个步骤：

- 1.open()函数，打开一个文件对象。
- 2.调用 read() 或 write() 方法进行读取文件内容    
- 3.调用 close() 关闭文件



### 1、写文件

```
# 声明一个方法来进行写入文件的操作，使用之际调用该方法即可
def write_file():
     print('------START-------')

     try:
         path = r'/Users/shaoboxue/Desktop/Python3Learn.txt’    # 使用字符串来保存路径

         f = open(path, 'w’)                                    # 进行打开操作
         f.write('Hello Python.’)                               # 写入操作

     except BaseException as e:
         print(e)

     finally:
         if f:
             f.close()                                          # 进行关闭操作
 
     print('------END-------')

```

### 2、读文件. 读取到的对象时以 list 的形式返回

```
# 声明一个读取文件的方法，使用之际调用该方法即可
def read_file():
     print('------START-------')

     try:
         path = r'/Users/shaoboxue/Desktop/Python3Learn.txt'
         f = open(path, 'r')
         print(f.readLines())

     except BaseException as e:
         print(e)

     finally:
         if f:
             f.close()

     print('------END-------')
     
```



### 3、读取二进制文件(图片、视频等)

```
# 声明一个读取二进制文件的方法，使用时直接调用该方法即可
def read_byte_file():

     try:
         path = r'/Users/shaoboxue/Desktop/001.png'
         f = open(path, ‘rb’)
         print(f.read())            # read() 一次性返回所有内容。readLines() 一行一行的读

     except BaseException as e:
         print(e)

     finally:
         if f:
             f.close()
             
```



### 4、字符编码

encoding 参数：读取非 UTF-8 编码的文本文件； 

errors 参数：遇到编码错误返回后如何处理，最简单的方式是直接忽略

```
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

path = r'/Users/shaoboxue/Desktop/001.png'

f = open(path, 'r', encoding='gbk', errors='ignore’)

# 参数1:文件的路径；参数2:需要进行的操作；参数3:编码格式；参数4:错误
```

